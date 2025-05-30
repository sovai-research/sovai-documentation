---
description: >-
  This section covers the usage of various short-selling datasets for risk
  analysis.
icon: sort-down
---

# Short Selling

{% hint style="info" %}
Data is updated weekly as data arrives after market close US-EST time.
{% endhint %}

{% hint style="success" %}
Dataset contains 5981+ tickers, available from 1998-01-02 onwards.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Short Selling Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Short%20Data.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Financial Intermediaries, NASDAQ, NYSE, CME</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing Techniques</td></tr><tr><td><strong>Model Outputs</strong></td><td>Predictions, Volume</td></tr></tbody></table>

## Description

This dataset provides comprehensive information on short-selling activity for various stocks, including metrics on short interest, volume, and related indicators.&#x20;

It offers investors and analysts insights into market sentiment, potential short squeezes, and overall risk assessment, enabling more informed decision-making in trading strategies and liquidity analysis.

## Data Access

### Over-shorted Dataset

The Over-Shorted dataset provides information on short interest and potentially over-shorted stocks, offering insights into short selling activity and related metrics.

#### Latest Data

```python
import sovai as sov
df_over_shorted = sov.data("short/over_shorted")
```

#### All Data

```python
import sovai as sov
df_over_shorted = sov.data("short/over_shorted", full_history=True)
```

### Short Volume Dataset

The Short Volume dataset offers information on the short selling volume for specified stocks, including breakdowns by different types of market participants.

#### Latest Data

```python
import sovai as sov
df_short_volume = sov.data("short/volume")
```

#### All Data

```python
import sovai as sov
df_short_volume = sov.data("short/volume", full_history=True)
```

### Accessing Specific Tickers

You can also retrieve data for specific tickers across these datasets. For example:

```python
df_ticker_over_shorted = sov.data("short/over_shorted", tickers=["AAPL", "MSFT"])
df_ticker_short_volume = sov.data("short/volume", tickers=["AAPL", "MSFT"])
```

## Data Dictionary

**Over-Shorted Dataset:**

| Column Name        | Description                             |
| ------------------ | --------------------------------------- |
| ticker             | Stock symbol                            |
| date               | Date of the data point                  |
| over\_shorted      | Measure of how over-shorted a stock is  |
| over\_shorted\_chg | Change in the over-shorted measure      |
| short\_interest    | Number of shares sold short             |
| number\_of\_shares | Total number of outstanding shares      |
| short\_percentage  | Percentage of float sold short          |
| short\_prediction  | Predicted short interest                |
| days\_to\_cover    | Number of days to cover short positions |
| market\_cap        | Market capitalization of the company    |
| total\_revenue     | Total revenue of the company            |
| volume             | Trading volume                          |



**Short Volume Dataset:**

| Column Name                    | Description                                           |
| ------------------------------ | ----------------------------------------------------- |
| ticker                         | Stock symbol                                          |
| date                           | Date of the data point                                |
| short\_volume                  | Volume of shares sold short                           |
| total\_volume                  | Total trading volume                                  |
| short\_volume\_ratio\_exchange | Ratio of short volume to total volume on the exchange |
| retail\_short\_ratio           | Ratio of short volume from retail traders             |
| institutional\_short\_ratio    | Ratio of short volume from institutional traders      |
| market\_maker\_short\_ratio    | Ratio of short volume from market makers              |

## Use Cases

* Short Squeeze Analysis: Identify potentially over-shorted stocks that might be candidates for a short squeeze.
* Risk Assessment: Evaluate the short interest in a stock as part of overall risk assessment.
* Market Sentiment Analysis: Use short volume data to gauge market sentiment towards specific stocks.
* Trading Strategy Development: Incorporate short selling data into quantitative trading strategies.
* Liquidity Analysis: Assess the liquidity of a stock by analyzing the days to cover metric.
* Sector Trends: Identify trends in short selling activity across different sectors or industries.



These datasets form a comprehensive toolkit for short selling analysis, enabling detailed examination of short interest, volume, and related metrics across different equities.
