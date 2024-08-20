---
description: >-
  The feature selection module in the sovai library provides various methods to
  identify and select the most important features from financial datasets.
icon: square-dashed-circle-plus
---

# Select Features

`Tutorials` are the best documentation — [<mark style="color:blue;">`Select Features Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/computational/Feature%20Selection.ipynb)

### Feature Selection Methods

The module supports several methods for feature selection, each based on different algorithms for determining feature importance. All methods use the `select_features` function with the following syntax:

```python
df_mega.select_features(method, n_components=10)
```

Where `method` is one of the following:

#### 1. Random Projection

```python
df_mega.select_features("random_projection", n_components=10)
```

Selects features based on their contribution to variance in the randomly projected space.

#### 2. Random Fourier Features

```python
df_mega.select_features("fourier", n_components=10)
```

Chooses features based on their influence on non-linear relationships in the Fourier-transformed space.

#### 3. Independent Component Analysis (ICA)

```python
df_mega.select_features("ica", n_components=10)
```

Selects features based on their contribution to extracted independent components, representing underlying independent signals in the data.

#### Truncated Singular Value Decomposition (SVD)

```python
df_mega.select_features("svd", n_components=10)
```

Chooses features based on their influence on principal singular vectors, which represent directions of maximum variance in the data.

#### Sparse Random Projection

```python
df_mega.select_features("sparse_projection", n_components=10)
```

Selects features based on their contribution to variance in the sparsely projected space, offering improved computational efficiency over standard Random Projection.

#### Clustered SHAP Ensemble

```python
df_mega.select_features("shapley", n_components=10)
```

Selects features using a method that iteratively applies clustering, uses XGBoost to predict cluster membership, calculates SHAP values, and averages results across multiple runs.

### Variability-based Selection

For all the models you can also select the number of components based on the total importance explained. When `variability` is specified:

```python
df_mega.select_features("random_projection", variability=0.80)
```

### Parameters

* `method`: String specifying the feature selection method (options listed above).
* `n_components`: Integer specifying the number of features to select (default is 10).
* If `variability` is provided, it must be a float between 0 and 1.

### Return Value

Each method returns a DataFrame containing the selected features and their corresponding data.

### Usage Notes

1. The `n_components` parameter allows you to control the number of features selected. Adjust this based on your specific needs and the total number of features in your dataset.
2. Different methods may yield different sets of selected features. It's often beneficial to compare results from multiple methods to gain a comprehensive understanding of feature importance.
3. The computational time may vary between methods. Some methods (like Sparse Random Projection) are designed for improved efficiency and may be preferable for larger datasets.
4. Always ensure you have sufficient historical data for reliable feature selection, especially when using methods that rely on capturing underlying data structures or relationships.
5. The selected features represent those deemed most important by each method. However, domain knowledge should also be considered when making final feature selection decisions for your specific application.
