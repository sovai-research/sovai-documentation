---
description: >-
  Implements multiple reduction techniques including PCA, SVD, Factor Analysis,
  Gaussian Random Projection, and UMAP.
---

# 🛹 Dimensionality Reduction

Reduction Techniques

The module supports the following dimensionality reduction methods:

* PCA (Principal Component Analysis)
* Factor Analysis
* Gaussian Random Projection
* UMAP (Uniform Manifold Approximation and Projection)

### Usage Examples

#### 1. Basic Usage with PCA

```python
import sovai as sov

# Authenticate and load data
sov.token_auth(token="your_token_here")
df_mega = sov.data("accounting/weekly").select_stocks("mega").date_range("2018-01-01")

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

### Advanced Usage

The underlying `dimensionality_reduction` function offers more control over the reduction process:

```python
from dimensionality_reduction import dimensionality_reduction

# Assuming df is your input DataFrame
result = dimensionality_reduction(df, method='pca', explained_variance=0.95, verbose=True)
print(result.head())
```

This advanced usage allows for specifying the amount of variance to be explained if `n_components` is not provided.

### Development Context

This module was developed to address the challenge of high-dimensional financial data. Key aspects of its development include:

1. Integration with `sovai`: The module is designed to work seamlessly with the `sovai` library, allowing easy loading of financial data.
2. Robust Preprocessing: The module includes comprehensive preprocessing steps to handle missing values, infinity values, and scaling, ensuring the data is suitable for dimensionality reduction.
3. Multiple Reduction Techniques: By implementing various reduction methods, the module provides flexibility for different types of analyses and data characteristics.
4. Performance Optimization: The use of efficient libraries like scikit-learn and UMAP ensures good performance even with large datasets.
5. Error Handling: The module includes extensive error checking and handling to provide informative feedback and maintain stability.
6. Maintaining Panel Data Structure: Special attention is given to preserving the panel data structure (ticker and date information) throughout the reduction process.

### Performance Considerations

* The dimensionality reduction process can be computationally intensive, especially for large datasets or when using methods like UMAP.
* PCA and Truncated SVD are generally faster than UMAP for large datasets.
* Consider using a smaller number of components or a subset of your data if performance is a concern.

Remember to refer to the `sovai` library documentation for more details on data loading and the specific financial metrics available.
