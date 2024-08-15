---
description: >-
  Clustering specifically designed for multivariate panel clustering of
  financial and time-series data
---

# 🍇 Clustering Panels

### Introduction

Can be used to cluster any panel dataset.  It is particularly useful for financial analysts, data scientists, and researchers working with time-series data across multiple entities (e.g., stocks, companies) and variables.

#### Initialization

The CustomDataFrame can be initialized using the `sov.data()` function:

```python
import sovai as sov

sov.token_auth(token="your_token_here")
df = sov.data("accounting/weekly")
```

Basic Clustering

Perform clustering on all features:

```python
df_cluster = df.cluster()
```

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

Feature-Specific Clustering

Cluster based on specific features:

```python
df_cluster_ebit = df.cluster(features=["ebit"])
df_cluster_multi = df.cluster(features=["total_assets", "total_debt", "ebit"])
```

#### Summary Clustering

Get a quick summary of the last 6-months data:

```python
df.cluster("summary")
```

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

### Visualization Methods

#### Line Plot

Visualize cluster centroids and distances:

```python
df.cluster("line_plot")
```

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>



**Scatter Plot**

Create a scatter plot of clustered data:

```python
df.cluster("scatter_plot")
```

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

#### Animation Plot

Generate an animated plot of cluster evolution:

```python
df.cluster("animation_plot")
```

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

### Advanced Analysis

#### Distance Calculation

Calculate distances between ticker-cluster combinations:

```python
df_dist = df_cluster.drop(columns=["labels"]).distance(orient="time-series")
```

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

### Examples

#### Basic Clustering and Visualization

```python
import sovai as sov

sov.token_auth(token="your_token_here")
df_accounting = sov.data("accounting/weekly")
df_mega = df_accounting.select_stocks("mega").date_range("2018-01-01")
df_cluster = df_mega.cluster()
df_mega.cluster("line_plot")
```

#### Feature-Specific Clustering and Distance Analysis

```python
df_cluster_ebit = df_mega.cluster(features=["ebit"])
df_dist = df_cluster_ebit.drop(columns=["labels"]).distance(orient="time-series")
similar_to_amzn = df_dist.sort_values(["AMZN"])[["AMZN"]].T
```
