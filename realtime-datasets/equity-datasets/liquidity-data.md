---
icon: water
description: >-
  Various dataset that could help with the assesment of security liquidity to
  inform trading decisions.
---

# Liquidity Data

{% hint style="info" %}
Data is updated weekly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Liquidity Data Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Liquidity%20Data.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Public Data from Financial Intermediaries</td></tr><tr><td><strong>Models Used</strong></td><td>Aggregate Calculations</td></tr><tr><td><strong>Model Outputs</strong></td><td>Price Improvement, Market Opportunity</td></tr></tbody></table>

***

## Description

This dataset provides comprehensive liquidity metrics for various stocks, including price improvement data and market making opportunities.&#x20;

It offers investors valuable insights into execution quality, liquidity risk, and market microstructure, enabling more informed trading decisions and strategy development across different market conditions and participant types.

## Data Access

#### Price Improvement Dataset

The latest Price Improvement dataset provides information on price improvements for various stocks, offering insights into trading execution quality.

```python
import sovai as sov
df_improve = sov.data("liquidity/price_improvement")
```

#### Market Opportunity Dataset

The latest Market Opportunity dataset offers information on market making opportunities and liquidity provision for different stocks.

```python
import sovai as sov
df_market = sov.data("liquidity/market_opportunity")
```

#### All data

The full history can be obtained using the `full_history=True` command:

```python
import sovai as sov
df_ticker_imp = sov.data("liquidity/price_improvement", full_history=True)
df_ticker_opp = sov.data("liquidity/market_opportunity", full_history=True)
```

#### Accessing Specific Tickers

You can also retrieve data for specific tickers across these datasets. For example:

```python
import sovai as sov
df_ticker_imp = sov.data("liquidity/price_improvement", tickers=["AAPL", "MSFT"])
df_ticker_opp = sov.data("liquidity/market_opportunity", tickers=["AAPL", "MSFT"])
```

## Data Dictionary

#### Price Improvement Dataset

| Column Name                    | Description                         |
| ------------------------------ | ----------------------------------- |
| ticker                         | Stock symbol                        |
| date                           | Date of the data point              |
| total\_price\_improvement      | Total price improvement amount      |
| shares                         | Number of shares traded             |
| price\_improvement\_per\_share | Average price improvement per share |
| average\_price\_improvement    | Average price improvement           |

#### Market Opportunity Dataset

| Column Name              | Description                                    |
| ------------------------ | ---------------------------------------------- |
| ticker                   | Stock symbol                                   |
| date                     | Date of the data point                         |
| missed\_liquidity        | Volume of missed liquidity opportunities       |
| exhausted\_liquidity     | Volume of exhausted liquidity                  |
| routed\_liquidity        | Volume of routed liquidity                     |
| volume\_opportunity      | Total volume opportunity                       |
| average\_daily\_vol      | Average daily trading volume                   |
| rolling\_daily\_vol      | Rolling average of daily trading volume        |
| buy\_pressure\_log       | Logarithmic measure of buying pressure         |
| buy\_pressure\_pct       | Percentage measure of buying pressure          |
| missed\_liquid\_pct      | Percentage of missed liquidity                 |
| exhausted\_liquid\_pct   | Percentage of exhausted liquidity              |
| vol\_uncaptured          | Percentage of uncaptured volume                |
| retail\_pressure         | Measure of retail trading pressure             |
| institutional\_pressure  | Measure of institutional trading pressure      |
| algorithmic\_pressure    | Measure of algorithmic trading pressure        |
| retail\_institute\_ratio | Ratio of retail to institutional pressure      |
| algo\_institute\_ratio   | Ratio of algorithmic to institutional pressure |
| retail\_algo\_ratio      | Ratio of retail to algorithmic pressure        |

## Use Cases

* Execution Quality Analysis: Evaluate the execution quality of trades using price improvement data.
* Market Making Strategies: Develop market making strategies based on liquidity provision opportunities.
* Liquidity Analysis: Assess the liquidity of a stock by analyzing various liquidity metrics.
* Trading Strategy Development: Incorporate liquidity data into quantitative trading strategies.
* Market Microstructure Analysis: Study market microstructure using detailed liquidity and price improvement data.
* Performance Benchmarking: Compare execution quality across different brokers or trading venues.
* Risk Management: Assess liquidity risk and potential transaction costs for large orders.
* Regulatory Compliance: Monitor best execution practices and demonstrate compliance with regulatory requirements.

These datasets form a comprehensive toolkit for liquidity analysis, enabling detailed examination of price improvements, liquidity provision, and related metrics across different market participants.

***
