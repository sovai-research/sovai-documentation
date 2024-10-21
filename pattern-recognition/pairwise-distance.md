---
icon: people-arrows
description: >-
  Pairwise statistics for distance and similarity between stocks in
  cross-section, time-series, and panel orientations.
---

# Pairwise Distance

`Tutorials` are the best documentation — [<mark style="color:blue;">`Pairwise Distance Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/computational/Pairwise%20Distance.ipynb)

## Pairwise Distance Statistics Module

`dataframe.distance()`

### Tutorial for Context.

### Features

* Cross-sectional distance calculations
* Time-series distance calculations
* Panel data distance calculations (Tucker decomposition)
* Multiple distance metrics and statistical tests

### Usage

The module is integrated into a custom DataFrame class, allowing for easy calculation of pairwise distances.&#x20;

```python
import sovai as sov

# Load data
df_factors = sov.data("factors/accounting")

# Select a subset of data
df_slice = df_factors.select_stocks("mega").date_range("2020-01-01")

# Calculate distances
dist_matrix = df_slice.distance()
```

<figure><img src="../.gitbook/assets/image (26).png" alt=""><figcaption></figcaption></figure>

### Distance Calculation Methods

#### 1. Cross-Sectional Distance

Calculates distances between stocks based on their attributes at each time point.

```python
dist_matrix = df_slice.distance(orient="cross-sectional", distance='cosine', calculations=features)
```

**Parameters:**

* `orient`: Set to "cross-sectional"
* `distance`: Distance metric (e.g., 'cosine', 'euclidean')
* **`calculations`**: List of features to include in the distance calculation

**Available Calculations:**

* `mean`: Average value
* `skew`: Skewness
* `std`: Standard deviation
* `diffm`: First difference mean
* `zcr`: Zero crossing rate
* `mac`: Mean absolute change
* `sc`: Spectral centroid
* `tp`: Turning points
* `acl1`: Autocorrelation at lag 1
* `hjorthm`: Hjorth mobility
* `hurst`: Hurst exponent
* `hist`: Histogram mode (5 bins)
* `timerev`: Time reversibility statistic

#### 2. Time-Series Distance

Computes distances between stocks based on their time-series behavior.

```python
dist_matrix = df_slice.distance(orient="time-series", metric="pearson")
```

**Parameters:**

* `orient`: Set to "time-series"
* **`metric`**: Distance metric to use

**Available Metrics:**

* `pearson`: Pearson correlation
* `spearman`: Spearman correlation
* `dtw`: Dynamic Time Warping
* `euclidean`: Euclidean distance
* `euclidean_int`: Euclidean distance with interpolation
* `pec`: Power Envelope Correlation
* `frechet`: Fréchet distance
* `kl_divergence`: Kullback-Leibler divergence
* `wasserstein`: Wasserstein distance
* `jaccard`: Jaccard distance
* `bray_curtis`: Bray-Curtis dissimilarity
* `hausdorff`: Hausdorff distance
* `manhattan`: Manhattan distance
* `chi2`: Chi-squared distance
* `hellinger`: Hellinger distance
* `canberra`: Canberra distance
* `shannon_entropy`: Shannon entropy-based distance
* `sample_entropy`: Sample entropy
* `approx_entropy`: Approximate entropy
* `jensen_shannon`: Jensen-Shannon divergence
* `renyi_entropy`: Rényi entropy
* `tsallis_entropy`: Tsallis entropy
* `mutual_information`: Mutual information-based distance

#### 3. Panel Data Distance

Utilizes Tucker decomposition to calculate distances considering both cross-sectional and time-series aspects.

```python
dist_matrix = df_slice.distance(orient="panel")
```

**Parameters:**

* `orient`: Set to "panel"

### Notes

* The module handles missing values by imputing them with the median.
* Some distance calculations may be computationally intensive for large datasets.
* The Tucker decomposition for panel data provides an estimated rank of the decomposition.

### Example

```python
# Calculate cross-sectional distances
dist_matrix_all = df_slice.distance(orient="cross-sectional", distance='cosine', calculations=features)

# Calculate time-series distances using Pearson correlation
dist_matrix_pearson = df_slice.distance(orient="time-series", metric="pearson")

# Calculate panel data distances
dist_matrix_tucker = df_slice.distance(orient="panel")
```

### Date instead of Ticker

While previous examples focused on calculating distances between stocks, we can also compute distances between dates using the same methods.&#x20;

This allows for analyzing how market conditions change over time.

### Converting to Date

All previous distance calculation functions can be modified to work with dates by specifying `on="date"`. Here are the key functions adapted for date-based analysis:

```python
# Mean distance between dates
dist_matrix_mean = df_slice.distance(on="date")

# Cross-sectional distances using cosine similarity
dist_matrix_cos = df_slice.distance(orient="cross-sectional", on="date", distance='cosine', calculations=features)

# Cross-sectional distances using Euclidean distance
dist_matrix_euc = df_slice.distance(orient="cross-sectional", on="date", distance='euclidean', calculations=features)

# Time-series distances using Pearson correlation
dist_matrix_pearson = df_slice.distance(orient="time-series", on="date", metric="pearson")

# Time-series distances using Dynamic Time Warping
dist_matrix_dtw = df_slice.distance(orient="time-series", on="date", metric="dtw")

# Time-series distances using Tsallis entropy
dist_matrix_tsent = df_slice.distance(orient="time-series", on="date", metric="tsallis_entropy")

# Panel data distances using Tucker decomposition
dist_matrix_tucker = df_slice.distance(orient="panel", on="date")
```

These functions calculate distances between different dates based on the market conditions or stock behaviors on those dates.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Sorting and Analyzing Date Distances

To analyze the distances for a specific date:

```python
date = dist_matrix_cos.index.max()
dist_matrix_cos.sort_values(date)[[date]].T
```

This code:

1. Selects the most recent date
2. Sorts the distances for that date
3. Displays the results as a transposed row

The output shows how similar or different market conditions on other dates were compared to the selected date, allowing for temporal analysis of market behavior.

This approach can help identify patterns, trends, or anomalous periods in market history by comparing the similarity of market conditions across different dates
