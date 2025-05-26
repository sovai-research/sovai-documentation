---
description: >-
  A very easily digestable dataframe format for all 10-K filings, with multiple
  sections, categories, and textual datapoints. This is not yet available, a
  work-in-progress.
icon: building-lock
---

# SEC 10K Filings

`Tutorials` are the best documentation — [<mark style="color:blue;">`Edgar Filings Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/studies/SEC%2010K%20Filings.ipynb)

{% hint style="success" %}
Dataset contains 4762+ tickers, available from 1998-03-31 onwards.
{% endhint %}

## Description

Annnual 10-K filings for which there are about 170,000 collected and processed.

## Data Access

#### SEC 10-Ks

```python
import sovai as sov
data = sov.data("sec/10k", tickers=["AAPL"], limit=1)
```

<figure><img src="../../.gitbook/assets/sec_10k_filings_1 (2).png" alt=""><figcaption></figcaption></figure>
