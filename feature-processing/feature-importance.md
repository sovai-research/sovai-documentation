---
description: >-
  The feature importance module in the sovai library offers multiple
  unsupervised algorithms to quantify the significance of each feature in
  financial datasets.
icon: ranking-star
---

# Feature Importance

`Tutorials` are the best documentation — [<mark style="color:blue;">`Feature Importance Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/computational/Feature%20Importance.ipynb)

### Feature Importance Methods

The module supports several methods for calculating feature importance:

#### Random Projection

```python
df_mega.importance("random_projection")
```

<figure><img src="../.gitbook/assets/image (95).png" alt=""><figcaption></figcaption></figure>

Reflects how much each feature contributes to the variance in the randomly projected space.

#### Random Fourier Features

```python
df_mega.importance("fourier")
```

Indicates how strongly each feature influences the approximation of non-linear relationships in the Fourier-transformed space.

#### Independent Component Analysis (ICA)

```python
df_mega.importance("ica")
```

Based on the magnitude of each feature's contribution to the extracted independent components, representing underlying independent signals in the data.

#### Truncated Singular Value Decomposition (SVD)

```python
df_mega.importance("svd")
```

Determined by each feature's influence on the principal singular vectors, which represent directions of maximum variance in the data.

#### Sparse Random Projection

```python
df_mega.importance("sparse_projection")
```

Based on how much each feature contributes to the variance in the sparsely projected space, similar to standard Random Projection but with improved computational efficiency.

#### Clustered SHAP Ensemble

```python
df_mega.importance("shapley")
```

Iteratively applies clustering, uses XGBoost to predict cluster membership, calculates SHAP values, and averages results across multiple runs to determine feature importance in identifying natural data structures.

### Global Feature Importance

To calculate global feature importance across all methods:

```python
df_mega.feature_importance()
```

### Feature Selection

Example of selecting top features based on importance scores:

```python
feature_importance = df_mega.importance("sparse_projection")
df_select = df_mega[feature_importance["feature"].head(25)]
```

<figure><img src="../.gitbook/assets/image (96).png" alt=""><figcaption></figcaption></figure>
