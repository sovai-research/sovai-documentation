---
description: >-
  Implements multiple reduction techniques including PCA, SVD, Factor Analysis,
  Gaussian Random Projection, and UMAP.
icon: reflect-horizontal
---

# Dimensionality Reduction

`Tutorials` are the best documentation — [<mark style="color:blue;">`Dimensionality Reduction Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/computational/Dimensionality%20Reduction.ipynb)

### Reduction Techniques

The module supports the following dimensionality reduction methods:

* PCA (Principal Component Analysis)
* Factor Analysis
* Gaussian Random Projection
* UMAP (Uniform Manifold Approximation and Projection)

### Usage Examples.

#### Authenticate and load data

```python
import sovai as sov
sov.token_auth(token="your_token_here")
df_mega = sov.data("accounting/weekly").select_stocks("mega").date_range("2018-01-01") 
```

#### 1. Basic Usage with PCA

```python
# Reduce dimensions using PCA
result = df_mega.reduce_dimensions(method="pca", n_components=10)
print(result.head())
```

#### 2. Using Gaussian Random Projection

```python
# Reduce dimensions using Gaussian Random Projection
result = df_mega.reduce_dimensions(method="gaussian_random_projection", n_components=10)
print(result.head())
```

#### 3. UMAP with Verbose Output

```python
# Reduce dimensions using UMAP with verbose output
result = df_mega.reduce_dimensions(method="umap", verbose=True, n_components=10)
print(result.head())
```

#### 4. Factor Analysis

```python
# Reduce dimensions using Factor Analysis with verbose output
result = df_mega.reduce_dimensions(method="factor_analysis", verbose=True, n_components=10)
print(result.head())
```

### Advanced Usage

The underlying `dimensionality_reduction` function offers more control over the reduction process:

```python
from dimensionality_reduction import dimensionality_reduction

# Assuming df is your input DataFrame
result = dimensionality_reduction(df, method='pca', explained_variance=0.95, verbose=True)
print(result.head())
```

This advanced usage allows for specifying the amount of variance to be explained if `n_components` is not provided.

### Performance Considerations

* The dimensionality reduction process can be computationally intensive, especially for large datasets or when using methods like UMAP.
* PCA and Truncated SVD are generally faster than UMAP for large datasets.
* Consider using a smaller number of components or a subset of your data if performance is a concern.
