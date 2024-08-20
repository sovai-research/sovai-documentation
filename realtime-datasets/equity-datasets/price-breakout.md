---
description: >-
  A dataset with daily updated predictions of price breaking upwards for US
  Equities.
icon: chart-line-up
---

# Price Breakout

{% hint style="info" %}
Daily predictions arrive between 11 pm - 4 am before market open in the US for 13,000+ stocks.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Price Breakout Prediction Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/tutorials/Breakout%20Prediction.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td>Input Datasets</td><td>Historical Stock Prices, Trading Volumes, Technical Indicators, Order Book.</td></tr><tr><td>Models Used</td><td>Classification Algorithms, Regression Models, Conformal Predictors</td></tr><tr><td>Model Outputs</td><td>Price Movement Predictions, Probability Scores, Confidence Intervals</td></tr></tbody></table>

This document provides guidance on utilizing the Breakout Prediction SDK to identify potential breakout stocks over the next 30-60 days for US Equities.

The accuracy is around 65% and ROC-AUC of 68%, it is one of the strongest price breakout models on the market.

## Data Access

### Retrieving Data

Fetch the latest breakout data using the SDK:

```python
from sovai import sov
df_breakout = sov.data("breakout").set_index("date")
```

### Today's Breakout Prediction

Access today's highest breakout stock predictions:

```python
# Filter for the latest date and sort by prediction values
df_breakout.get_latest()
```

<figure><img src="../../.gitbook/assets/image (10) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Retrieve Specific Ticker Data

Get breakout data for a specific ticker such as Microsoft (MSFT):

```python
df_msft = sov.data("breakout", tickers=["MSFT"])
```

## Plots

### **Line Predictions**

```python
df_breakout.plot_line(tickers=["TSLA", "META", "NFLX"])
```

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Breakout Predictions

Visualize breakout predictions using the SDK's plotting capabilities:

```python
sov.plot("breakout", chart_type="predictions", df=df_msft)
```

<figure><img src="../../.gitbook/assets/image (16) (1).png" alt=""><figcaption></figcaption></figure>

### Prediction Accuracy

Assess the accuracy of breakout predictions:

```python
sov.plot("breakout", chart_type="accuracy", df=df_msft)
```

<figure><img src="../../.gitbook/assets/image (17) (1).png" alt=""><figcaption></figcaption></figure>

## Data Dictionary

<table><thead><tr><th width="237">Column</th><th>Description</th><th>Type</th><th>Example</th></tr></thead><tbody><tr><td><code>ticker</code></td><td>Stock ticker symbol.</td><td>object</td><td>"AAPL"</td></tr><tr><td><code>date</code></td><td>Date when the data was recorded.</td><td>datetime64[ns]</td><td>2023-09-30</td></tr><tr><td><code>target</code></td><td>Target variable for predictions.</td><td>float64</td><td>0.05</td></tr><tr><td><code>future_returns</code></td><td>Future returns of the stock.</td><td>float32</td><td>0.10</td></tr><tr><td><code>prediction</code></td><td>Predicted probability from the model.</td><td>float64</td><td>1.25</td></tr><tr><td><code>bottom_prediction</code></td><td>Lower bound of the prediction interval.</td><td>float64</td><td>1.20</td></tr><tr><td><code>top_prediction</code></td><td>Upper bound of the prediction interval.</td><td>float64</td><td>1.30</td></tr><tr><td><code>standard_deviation</code></td><td>Standard deviation of the predictions.</td><td>float64</td><td>0.02</td></tr><tr><td><code>bottom_conformal</code></td><td>Lower bound of the conformal prediction interval.</td><td>float64</td><td>1.18</td></tr><tr><td><code>top_conformal</code></td><td>Upper bound of the conformal prediction interval.</td><td>float64</td><td>1.32</td></tr><tr><td><code>slope</code></td><td>Slope derived from the rolling regression of predictions over a window.</td><td>float64</td><td>0.003</td></tr></tbody></table>

***

## **Description**

***

### Prediction Model for Price Increases

This document outlines the prediction model used to forecast stock price movements. The model employs a variety of machine learning techniques and is optimized for equity selection. With an emphasis on pricing information, it is designed to predict significant price increases with high accuracy.

### Model Description

The model is constructed using a series of Python-based machine learning algorithms, with data processing and feature engineering steps to prepare the data for analysis.

#### Data Preparation

Data is initially sourced from a BigQuery table containing historical pricing information, such as adjusted close prices and trading volume. The data is preprocessed to generate features that capture historical trends and patterns, including:

* **Return Features**: Percent changes in price and volume over specified time windows.
* **Rolling Features**: Rolling statistics (mean, standard deviation, skewness, etc.) calculated over different periods to capture short- and long-term movements.
* **Date Features**: Time-based features to account for seasonal trends and temporal patterns.
* **Target Variable**: A binary classification target indicating whether the stock price will see a significant increase (`1`) or decrease (`0`) over a given time horizon.

#### Feature Engineering

The model includes extensive feature engineering to enhance the predictive power of the training data:

* **Standardized Returns**: The return of a stock over a specified period divided by the rolling standard deviation of the return, offering a normalized measure of price movement.
* **Summary Statistics**: Aggregated metrics derived from the newly created lagged return features, providing a comprehensive view of recent price behavior.

#### Model Training

Several machine learning models are trained using the prepared dataset:

* **Calibrated Classifier**: A classification model trained on the engineered features to predict the binary target.
* **Proprietory Regressor**: A proprietory regression model is used to predict the probability of a price increase.
* **Conformal Regressor**: Used to provide calibrated confidence intervals around the predictions, offering an additional measure of uncertainty.

#### Model Usage

The model can be applied to new data to generate predictions for the likelihood of price increases. It utilizes the trained classifiers and regressors to provide both point estimates and confidence intervals for these predictions.
