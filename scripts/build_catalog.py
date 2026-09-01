#!/usr/bin/env python3
"""Resolve the dataset-catalog SOURCE and write a normalized ``scripts/catalog.json``.

This is the ONE place that decides where the served-surface facts come from, so
the docs generator (``gen_catalog_docs.py``) renders from a committed snapshot.
It is the twin of ``sovai-website/internals/scripts/build_catalog.py`` — keep
the two in step.

Source resolution (first that is available wins)
------------------------------------------------
1. ``SOVAI_CATALOG_JSON`` — a path to a JSON file that is either an
   already-normalized catalog (top-level ``datasets``) or the frozen global
   ``sovai-catalog/index.json`` (``CatalogIndex``, top-level ``catalogs``).
2. ``SOVAI_CATALOG_URL`` — an http(s) URL to the same, fetched read-only.
3. otherwise a LOCAL derivation from the producer repo's IMMUTABLE contracts
   (``self-cleaning-new/src/pipelines/*/contracts/endpoint_config.py`` plus the
   pandera schemas that ``selfclean/serving/column_dict.py`` reads). The
   producer repo is found via ``SELFCLEAN_REPO`` or by walking up to the
   ``sovai-universe`` container. This path needs the producer's Python env.

The catalog is NOT yet populated in R2 (no producer export has run), so path 3
is the reliable offline source today; paths 1/2 take over the day the live
catalog exists. Output carries NO wall-clock timestamp, so re-deriving from
unchanged contracts is byte-identical and ``--check`` is a real drift gate.

Usage
-----
    python scripts/build_catalog.py            # write scripts/catalog.json
    python scripts/build_catalog.py --check    # exit 1 if that file is stale
    python scripts/build_catalog.py --stdout   # print, write nothing
"""
from __future__ import annotations

import argparse
import importlib
import json
import os
import re
import sys
import urllib.request
from pathlib import Path
from typing import Any

NORMALIZED_SCHEMA_VERSION = "1.0.0"

_HERE = Path(__file__).resolve()
_REPO_ROOT = _HERE.parent.parent  # scripts/ -> repo root
_OUT_PATH = _REPO_ROOT / "scripts" / "catalog.json"


def _producer_repo() -> Path:
    env = os.environ.get("SELFCLEAN_REPO")
    if env:
        return Path(env).expanduser().resolve()
    for parent in _HERE.parents:
        cand = parent.parent / "self-cleaning-new"
        if cand.is_dir():
            return cand.resolve()
        cand = parent / "self-cleaning-new"
        if cand.is_dir():
            return cand.resolve()
    return Path("self-cleaning-new")


def _short_dtype(dtype: str | None) -> str | None:
    if dtype is None:
        return None
    if dtype.startswith("Datetime"):
        m = re.search(r"time_unit='([^']+)'", dtype)
        return f"Datetime[{m.group(1)}]" if m else "Datetime"
    return dtype


def _derive_from_producer(producer_repo: Path) -> dict[str, Any]:
    src = producer_repo / "src"
    if not src.is_dir():
        raise SystemExit(
            f"producer repo not found at {producer_repo} (set SELFCLEAN_REPO). "
            "Cannot derive the catalog and no SOVAI_CATALOG_JSON/URL was given."
        )
    if str(src) not in sys.path:
        sys.path.insert(0, str(src))

    from selfclean.pipelines import all_pipelines, discover
    from selfclean.serving import manifest as manifest_mod
    from selfclean.serving.column_dict import columns_for_endpoint, compile_schemas

    try:
        from selfclean.serving import schema as schema_mod

        versions = {
            "manifest_version": schema_mod.MANIFEST_VERSION,
            "index_version": schema_mod.INDEX_VERSION,
        }
    except Exception:
        versions = {"manifest_version": "unknown", "index_version": "unknown"}

    discover()
    datasets: list[dict[str, Any]] = []
    for pipeline in all_pipelines():
        name = str(pipeline.name)
        try:
            mod = importlib.import_module(f"pipelines.{name}.contracts.endpoint_config")
        except Exception:
            continue
        cfg = getattr(mod, "ENDPOINT_CONFIG", None)
        if not isinstance(cfg, dict):
            continue
        try:
            bucket = manifest_mod._serving_bucket(name, mod)
        except Exception:
            bucket = getattr(mod, "SERVING_BUCKET", "") or ""
        schemas = compile_schemas(name)
        for endpoint, spec in cfg.items():
            spec_d = dict(spec) if isinstance(spec, dict) else {}
            folder = spec_d.get("folder")
            cols = columns_for_endpoint(schemas, str(endpoint), folder=folder)
            columns = [
                {
                    "name": c.name,
                    "dtype": _short_dtype(c.dtype),
                    "nullable": bool(c.nullable),
                    "description": c.description or "",
                    "unit": c.unit or "",
                }
                for c in cols
            ]
            has_ticker = bool(spec_d.get("has_ticker_path", False)) or bool(
                spec_d.get("partition_cols_ticker") or spec_d.get("partition_col_ticker")
            )
            has_date = bool(spec_d.get("has_date_path", False)) or bool(
                spec_d.get("partition_cols_date") or spec_d.get("partition_col_date")
            )
            datasets.append(
                {
                    "endpoint": str(endpoint),
                    "pipeline": name,
                    "serving_bucket": bucket,
                    "column_count": len(columns),
                    "columns": columns,
                    "provenance": {
                        "has_ticker_path": has_ticker,
                        "has_date_path": has_date,
                        "has_year": bool(spec_d.get("has_year", False)),
                        "folder": folder,
                    },
                    "freshness": {
                        "verdict": "unknown",
                        "cadence": None,
                        "watermark": None,
                        "note": "populated from the live per-bucket manifest once a producer export runs",
                    },
                }
            )

    datasets.sort(key=lambda d: d["endpoint"])
    return {
        "normalized_schema_version": NORMALIZED_SCHEMA_VERSION,
        "source": "producer-contracts",
        "producer_versions": versions,
        "datasets": datasets,
    }


def _load_live(raw: str, *, is_url: bool) -> dict[str, Any]:
    if is_url:
        with urllib.request.urlopen(raw, timeout=30) as resp:  # noqa: S310
            doc = json.loads(resp.read().decode("utf-8"))
    else:
        doc = json.loads(Path(raw).expanduser().read_text())

    if isinstance(doc, dict) and isinstance(doc.get("datasets"), list):
        doc.setdefault("normalized_schema_version", NORMALIZED_SCHEMA_VERSION)
        doc.setdefault("source", "live-normalized")
        return doc

    if isinstance(doc, dict) and isinstance(doc.get("catalogs"), dict):
        datasets: list[dict[str, Any]] = []
        for pipeline, entry in doc["catalogs"].items():
            bucket = str(entry.get("serving_bucket", ""))
            for endpoint in entry.get("endpoints", []):
                datasets.append(
                    {
                        "endpoint": str(endpoint),
                        "pipeline": str(pipeline),
                        "serving_bucket": bucket,
                        "column_count": 0,
                        "columns": [],
                        "provenance": {},
                        "freshness": {
                            "verdict": "unknown",
                            "cadence": None,
                            "watermark": None,
                            "note": "CatalogIndex lists endpoints only; per-bucket manifests carry columns/freshness",
                        },
                    }
                )
        datasets.sort(key=lambda d: d["endpoint"])
        return {
            "normalized_schema_version": NORMALIZED_SCHEMA_VERSION,
            "source": "live-catalog-index",
            "producer_versions": {"index_version": str(doc.get("index_version", "unknown"))},
            "datasets": datasets,
        }

    raise SystemExit(
        "SOVAI_CATALOG_JSON/URL did not look like a normalized catalog "
        "(top-level 'datasets') nor a CatalogIndex (top-level 'catalogs')."
    )


def resolve_catalog() -> dict[str, Any]:
    path = os.environ.get("SOVAI_CATALOG_JSON")
    if path:
        return _load_live(path, is_url=False)
    url = os.environ.get("SOVAI_CATALOG_URL")
    if url:
        return _load_live(url, is_url=True)
    return _derive_from_producer(_producer_repo())


def _serialize(catalog: dict[str, Any]) -> str:
    return json.dumps(catalog, indent=2, ensure_ascii=False, sort_keys=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="exit 1 if scripts/catalog.json is stale")
    parser.add_argument("--stdout", action="store_true", help="print instead of writing")
    args = parser.parse_args()

    body = _serialize(resolve_catalog())

    if args.stdout:
        sys.stdout.write(body)
        return 0
    if args.check:
        current = _OUT_PATH.read_text() if _OUT_PATH.exists() else ""
        if current != body:
            sys.stderr.write(
                "scripts/catalog.json is STALE relative to the catalog source. "
                "Regenerate with `python scripts/build_catalog.py`.\n"
            )
            return 1
        print("scripts/catalog.json is up to date.")
        return 0

    _OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    _OUT_PATH.write_text(body)
    print(f"wrote scripts/catalog.json ({len(json.loads(body)['datasets'])} endpoints)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
