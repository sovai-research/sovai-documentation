---
description: >-
  The feature extractor module generates features that can be categorized into
  several types based on the nature of the calculations.
---

# 🛹 Extract Features

## Feature Extraction Module

This module provides powerful feature extraction capabilities for time series data, particularly focused on financial and accounting metrics. It leverages the `sovai` library for data retrieval and a custom `feature_extractor` function for generating a wide range of statistical and time series features.

### Feature Categories

The `feature_extractor` generates features that fall into several categories:

* Statistical Features
* Entropy and Complexity Features
* Frequency and Streak Features
* Energy and Magnitude Features
* Distributional Features
* Position Features

### Usage Examples

```python
import sovai as sov

# Authenticate and load data
sov.token_auth(token="your_token_here")
df_mega = sov.data("accounting/weekly").select_stocks("mega").date_range("2018-01-01")
```

#### 1. Basic Usage with Default Parameters

```python
# Extract features with default parameters
result = df_mega.extract_features(every="all")
print(result.head())
```

<figure><img src="../.gitbook/assets/image (77).png" alt=""><figcaption></figcaption></figure>

#### 2. Weekly Rolling Features

```python
# Extract features with a 12-week lookback, calculated weekly
result = df_mega.extract_features(lookback=12, every='week')
print(result.head())
```

#### 3. Custom Feature List

```python
# Extract specific features with custom parameters
custom_features = ["operating_working_capital", "cash_short_term"]
result = df_mega.extract_features(lookback=12, every='week', features=custom_features)
print(result.head())
```

#### 4. Monthly Rolling Features

```python
# Use monthly rolling features with a 2-month lookback
result = df_mega.extract_features(lookback='2mo', every='month')
print(result.head())
```

### Advanced Usage

The underlying `feature_extractor` function offers more granular control over the feature extraction process. It can be used directly for more advanced use cases:

```python
import polars as pl
from feature_extractor import feature_extractor

# Assuming df is your input DataFrame
result = feature_extractor(df, entity_col='ticker', date_col='date', 
                           lookback='1mo', every='week', verbose=True)
print(result.head())
```

This advanced usage allows for more customization, including specifying entity and date columns, adjusting lookback periods, and enabling verbose output for debugging.

#### Statistical Features

* **Mean and Variance Related:**
  * `mean_abs_change`
  * `variation_coefficient`
  * `mean_change`
  * `mean_second_derivative_central`

#### Entropy and Complexity Features

* **Entropy:**
  * `binned_entropy`
* **Complexity:**
  * `lempel_ziv_complexity`

#### Frequency and Streak Features

* **Frequency:**
  * `number_crossings`
  * `number_peaks`
* **Streak:**
  * `longest_streak_above_mean`
  * `longest_losing_streak`
  * `longest_winning_streak`

#### Energy and Magnitude Features

* **Energy:**
  * `absolute_energy`
* **Magnitude:**
  * `absolute_maximum`
  * `absolute_sum_of_changes`
  * `max_abs_change`

#### Statistical and Distributional Features

* **Statistical:**
  * `root_mean_square`
  * `ratio_beyond_r_sigma`
* **Distributional:**
  * `benford_correlation`
  * `percent_reoccurring_points`
  * `percent_reoccurring_values`

#### Position Features

* **Positions:**
  * `first_location_of_maximum`
  * `first_location_of_minimum`
  * `last_location_of_maximum`
  * `last_location_of_minimum`

These categories help organize the wide range of features generated, which capture different aspects of the time series data, making them useful for various analytical and predictive tasks.
