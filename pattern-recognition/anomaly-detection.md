---
description: >-
  It provides methods to detect global, local, and cluster anomalies in
  multivariate financial data
---

# 🏰 Anomaly Detection

### Key Features

1. Multiple anomaly detection methods:
   * Global anomalies: Identify outliers considering the entire dataset
   * Local anomalies: Detect outliers within local neighborhoods
   * Cluster anomalies: Find anomalies considering multi-dimensional data structure
2. Anomaly scoring: Compute anomaly scores for each data point
3. Feature-level anomaly analysis: Identify the most anomalous features for a given security

### Usage

Load the accounting factors data:

```python
import pandas as pd

df_factors = sov.data("factors/accounting", purge_cache=True)
df_last_3_years = df_factors.loc[(slice(None), slice(pd.Timestamp.now() - pd.DateOffset(years=3), None)), :]
df_last_3_years = df_last_3_years.percentile()
```

### Anomaly Detection

#### Compute Anomaly Scores

<pre class="language-python"><code class="lang-python"><strong>df_anomaly_scores = df_last_3_years.anomalies("scores", ticker="TSLA")
</strong></code></pre>

<figure><img src="../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Local Anomalies

```python
df_local = df_last_3_years.anomalies("local", ticker="NVDA")
```

<figure><img src="../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Global Anomalies

```python
df_global = df_last_3_years.anomalies("global", ticker="NVDA")
```

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Cluster Anomalies

```python
df_cluster = df_last_3_years.anomalies("cluster", ticker="NVDA")
```

<figure><img src="../.gitbook/assets/image (6) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Notes

* The module uses the `sovai` library for data loading and processing. Ensure you have the necessary permissions and valid authentication token.
* Anomaly detection methods can be applied to different time ranges and tickers. Adjust the parameters as needed for your analysis.
* The module provides flexibility in analyzing anomalies at both the overall and feature level. Experiment with different combinations of methods for comprehensive insights.
* When working with large datasets, be mindful of computational resources, especially when applying multiple anomaly detection methods or creating complex visualizations.
