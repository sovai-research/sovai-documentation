---
description: >-
  Earnings announcements are obtained from external sources as well as estimate
  information leading up to the actual announcement.
icon: users-between-lines
---

# Earnings Surprise

{% hint style="info" %}
Data arrives late Friday night 11 pm - 12; the model also retrains weekly.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Earnings Surprise Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Earnings%20Surprise.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Public filings, news, analyst reports</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Regex</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Rows</td></tr></tbody></table>

{% hint style="success" %}
Dataset contains 4330+ tickers, available from 2016-12-30 onwards.
{% endhint %}

## Description

The **Earnings Surprise** dataset provides detailed insights into the financial performance of publicly traded companies by capturing the discrepancies between reported earnings and analysts' estimates. This dataset includes metrics such as the probability of an earnings surprise, the magnitude of earnings per share (EPS) surprises, actual earnings results, estimated earnings, and the publication dates of earnings reports.

By offering a granular view of earnings performance, this data serves as a vital tool for investors to assess company performance, predict stock price movements, and make informed investment decisions based on the reliability and accuracy of earnings forecasts.

## Data Access

```python
import sovai as sov
df_earn_surp = sov.data("earnings/surprise", tickers=["AAPL", "MSFT"])
```

<figure><img src="../../.gitbook/assets/earnings_surprise_1 (2).png" alt=""><figcaption></figcaption></figure>

## Data Dictionary

| **Name**                | **Description**                               | **Type** | **Example**           |
| ----------------------- | --------------------------------------------- | -------- | --------------------- |
| `ticker`                | Stock ticker symbol of the company            | object   | `AAPL`                |
| `date`                  | Date of the earnings report                   | object   | `2016-12-30`          |
| `surprise_probability`  | Probability of an earnings surprise occurring | float64  | `-0.496`              |
| `eps_surprise`          | Earnings per share surprise value             | float64  | `0.040`               |
| `actual_earning_result` | Actual reported earnings per share            | float64  | `0.840`               |
| `estimated_earning`     | Analysts' estimated earnings per share        | float64  | `0.800`               |
| `date_pub`              | Publication date of the earnings report       | object   | `2017-01-31T00:00:00` |
| `market_cap`            | Market capitalization of the company (in USD) | float64  | `1.5e+12`             |

***

## Use Cases

* **Investment Signal Generation:** Utilize earnings surprise metrics to identify potential investment opportunities by spotting companies that consistently outperform or underperform earnings expectations.
* **Risk Management:** Assess the risk associated with investments by monitoring the frequency and magnitude of earnings surprises, identifying companies with unstable earnings.
* **Event-Driven Investment Strategies:** Develop strategies around earnings report dates, capitalizing on anticipated surprises to execute buy or sell orders based on expected market reactions.

***
