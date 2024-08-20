---
description: >-
  This dataset provides historical and forecasted risk-parity asset allocation
  data for investors for five asset classes.
---

# 🏳️ Asset Rotation

{% hint style="info" %}
Monthly allocation estimates for five assets.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Asset Rotation Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Asset%20Rotation%20and%20Allocation.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td>Input Datasets</td><td>Hundreds of economic indicators</td></tr><tr><td>Models Used</td><td>Imputation Models, Machine Learning</td></tr><tr><td>Model Outputs</td><td>Optimal Allocations</td></tr></tbody></table>

The dataset covers five asset classes: bonds, equities, commodities, dollar, and real estate. The data is presented in a monthly frequency, starting from November 1959.&#x20;

### Data Access

#### Returns All

Return predictions, historically and 8-years in the future.

```python
from sovai import sov 
df_returns = sov.data("allocation/returns")
```

#### Allocation All

Historical allocations and future risk-parity allocations

```python
from sovai import sov 
df_allocate = sov.data("allocation/all")
```

### Plot Access

#### Line Plot

Looking at the future and past prescribed allocations over-time

```python
from sovai import sov 
sov.plot("allocation", "line")
```

<figure><img src="../../.gitbook/assets/image (114).png" alt=""><figcaption></figcaption></figure>

#### Stacked Plot

Looking at the future and past prescribed allocations over-time

```python
from sovai import sov 
sov.plot("allocation", "stacked")
```

<figure><img src="../../.gitbook/assets/image (115).png" alt=""><figcaption></figcaption></figure>

***
