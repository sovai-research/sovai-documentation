---
description: >-
  This module allows users to apply various filters and screens to a
  comprehensive dataset of financial and market factors.
---

# 📉 Screens and Filters

## Screens and Filters Module

### Overview

The Screens and Filters module is a versatile component of the sovai software suite, designed to help investors and analysts identify novel investment opportunities using a wide range of features as filtering and selection criteria.&#x20;

### Key Features

* Access to hundreds of financial and market factors
* Ability to filter based on latest data points
* Stock selection by market capitalization categories
* Flexible querying capabilities
* Chaining of multiple filters and selections

### Usage

To use the Screens and Filters module, you first need to authenticate and then you can start applying various filters and screens to the data. Here's an example of how to use this module:

```python
import sovai as sov

# Authenticate
sov.token_auth(token="your_authentication_token")

# Load comprehensive factor data
df_comprehensive = sov.data("factors/comprehensive")
```

### Available Methods and Functionality

#### 1. Get Latest Data

```python
df_risk = df_comprehensive.get_latest("business_risk")[["business_risk"]]
```

This method allows you to extract the most recent data point for a specific factor.

#### 2. Select Stocks by Market Cap

```python
df_mega = df_risk.select_stocks("mega")
```

This method filters stocks based on market capitalization category. In this example, it selects only mega-cap stocks.

#### 3. Apply Custom Queries

```python
df_ten = df_mega.query("business_risk <= 10")
```

This method allows you to apply custom filtering conditions using familiar Python query syntax.

#### 4. Chaining Operations

You can chain multiple operations together for more complex screening:

```python
df_ten = (sov.data("factors/comprehensive")
          .get_latest("business_risk")[["business_risk"]]
          .select_stocks("mega")
          .query("business_risk <= 10"))
```

This chain of operations:

1. Loads the comprehensive factor data
2. Selects the latest "business\_risk" factor
3. Filters for mega-cap stocks
4. Applies a custom query to select stocks with business risk <= 10

### Example Use Case

Let's walk through an example of using the Screens and Filters module to identify large-cap companies with low business risk sensitivity:

```python
import sovai as sov

# Authenticate
sov.token_auth(token="your_authentication_token")

# Load data, filter for mega-caps with business risk <= 10
df_filtered = (sov.data("factors/comprehensive")
               .get_latest("business_risk")[["business_risk"]]
               .select_stocks("mega")
               .query("business_risk <= 10"))

print(df_filtered)
```

This script will return a DataFrame containing mega-cap stocks with a business risk sensitivity of 10% or less, based on the most recent data point.

### Conclusion

The Screens and Filters module provides a powerful and flexible way to identify investment opportunities based on a wide range of factors. By combining different filtering methods and leveraging the extensive factor database, users can create sophisticated screening strategies to suit their investment criteria.
