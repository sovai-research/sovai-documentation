---
icon: building-lock
description: >-
  A very easily digestable dataframe format for all 10-K filings, with multiple
  sections, categories, and textual datapoints.
---

# SEC 10K Filings

`Tutorials` are the best documentation — [<mark style="color:blue;">`Edgar Filings Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/studies/SEC%2010K%20Filings.ipynb)

## Description

Annnual 10-K filings for which there are about 170,000 collected and processed.

## Data Access

#### SEC 10-Ks

```python
import sovai as sov
data = sov.data("sec/10k", tickers=["AAPL"], limit=1)
```

<figure><img src="../../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>
