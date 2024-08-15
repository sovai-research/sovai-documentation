---
description: >-
  Clustering specifically designed for multivariate panel clustering of
  financial and time-series data
---

# 🍇 Clustering Panels

### 1. Introduction

Can be used to cluster any panel dataset.  It is particularly useful for financial analysts, data scientists, and researchers working with time-series data across multiple entities (e.g., stocks, companies) and variables.

### 2. Installation

To install the CustomDataFrame module, use pip:

```
pip install sovai
```

Note: The module is part of the `sovai` package.

### 3. Module Overview

The CustomDataFrame module builds upon pandas' DataFrame to offer specialized functionality for multivariate panel data analysis and clustering.

Key features include:

* Efficient handling of panel data structures
* Built-in multivariate clustering algorithms
* Support for various data types (e.g., accounting data, stock prices)
* Visualization tools for cluster analysis
* Advanced time-series analysis capabilities

### 4. Class: CustomDataFrame

The CustomDataFrame class is the core of this module, extending the functionality of pandas DataFrame.

#### 4.1 Initialization

The CustomDataFrame can be initialized using the `sov.data()` function:

```python
import sovai as sov

sov.token_auth(token="your_token_here")
df = sov.data("accounting/weekly")
```

### 5. Data Loading and Preprocessing

#### 5.1 Loading Data

```python
df = sov.data("accounting/weekly")
```

#### 6.1 Basic Clustering

Perform clustering on all features:

```python
df_cluster = df.cluster()
```

<figure><img src="../.gitbook/assets/image (100).png" alt=""><figcaption></figcaption></figure>

#### 6.2 Feature-Specific Clustering

Cluster based on specific features:

```python
df_cluster_ebit = df.cluster(features=["ebit"])
df_cluster_multi = df.cluster(features=["total_assets", "total_debt", "ebit"])
```

#### 6.3 Summary Clustering

Get a quick summary of the last 6-months data:

```python
df.cluster("summary")
```

<figure><img src="../.gitbook/assets/image (105).png" alt=""><figcaption></figcaption></figure>

### 7. Visualization Methods

#### 7.1 Line Plot

Visualize cluster centroids and distances:

```python
df.cluster("line_plot")
```

<figure><img src="../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>

#### 7.2 Scatter Plot

Create a scatter plot of clustered data:

```python
df.cluster("scatter_plot")
```

<figure><img src="../.gitbook/assets/image (109).png" alt=""><figcaption></figcaption></figure>

#### 7.3 Animation Plot

Generate an animated plot of cluster evolution:

```python
df.cluster("animation_plot")
```

<figure><img src="../.gitbook/assets/image (110).png" alt=""><figcaption></figcaption></figure>

### 8. Advanced Analysis

#### 8.1 Distance Calculation

Calculate distances between ticker-cluster combinations:

```python
df_dist = df_cluster.drop(columns=["labels"]).distance(orient="time-series")
```

<figure><img src="../.gitbook/assets/image (111).png" alt=""><figcaption></figcaption></figure>

### 9. Examples

#### 9.1 Basic Clustering and Visualization

```python
import sovai as sov

sov.token_auth(token="your_token_here")
df_accounting = sov.data("accounting/weekly")
df_mega = df_accounting.select_stocks("mega").date_range("2018-01-01")
df_cluster = df_mega.cluster()
df_mega.cluster("line_plot")
```

#### 9.2 Feature-Specific Clustering and Distance Analysis

```python
df_cluster_ebit = df_mega.cluster(features=["ebit"])
df_dist = df_cluster_ebit.drop(columns=["labels"]).distance(orient="time-series")
similar_to_amzn = df_dist.sort_values(["AMZN"])[["AMZN"]].T
```
