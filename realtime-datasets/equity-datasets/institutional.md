---
description: >-
  The dataset provides a comprehensive analysis of institutional investment
  behaviors, strategies, and portfolio dynamics assist professional investors in
  making informed decisions.
---

# 🏦 Institutional Trading

{% hint style="info" %}
Data is updated quarterly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — <mark style="color:blue;">`Financial Ratio Analysis`</mark>

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>13F Filings, Market Data</td></tr><tr><td><strong>Models Used</strong></td><td>Simple Calculations, Aggregations</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Ratios</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

## Data Access

#### Institutional Trading Data

This data is around 1GB if you download the entire dataset.

```python
from sovai import sov
df_institute = sov.data("institutional/trading")
```

<figure><img src="../../.gitbook/assets/image (19) (1).png" alt=""><figcaption></figcaption></figure>

#### Filtered Dataset

```python
from sovai import sov
df_institute = sov.data("institutional/trading", start_date="2004-04-30", tickers=["MSFT"])
```

## Reports

### Grouped ranking

```python
import sovai as sov
sov.report("institutional/flow_prediction", report_type="ranking")
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Plots

### Institutional Flow Prediction

```python
import sovai as sov
sov.plot("institutional", chart_type="prediction")
```

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Grouped Plot

```python
import sovai as sov
sov.plot("institutional", chart_type="flows")
```

<figure><img src="../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption><p>Highlighting certain sectors</p></figcaption></figure>

## Data Dictionary

<table><thead><tr><th width="340">Name</th><th width="329">Description</th><th>Type</th></tr></thead><tbody><tr><td>std_percentoftotal_fund_median</td><td>Rolling standard deviation of 'percentoftotal' over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>std_put_call_ratio_fund_median</td><td>Rolling standard deviation of the put-call ratio over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>std_derivative_ratio_fund_median</td><td>Rolling standard deviation of the derivative ratio over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>derivative_ratio_fund_median</td><td>Ratio of the sum of put value and call value to share value for each investor.</td><td>float64</td></tr><tr><td>put_call_ratio_fund_median</td><td>Put-call ratio calculated as the difference between put value and call value divided by their sum for each investor.</td><td>float64</td></tr><tr><td>fund_ratio_fund_median</td><td>Ratio of fund value to share value for each investor.</td><td>float64</td></tr><tr><td>debt_ratio_fund_median</td><td>Ratio of debt value to share value for each investor.</td><td>float64</td></tr><tr><td>preferred_ratio_fund_median</td><td>Ratio of preferred stock value to share value for each investor.</td><td>float64</td></tr><tr><td>totalvalue_median</td><td>Median of the total value of holdings for each investor.</td><td>float64</td></tr><tr><td>percentoftotal_median</td><td>Median of the percentage of total holdings for each investor.</td><td>float64</td></tr><tr><td>shrholdings_growth_median</td><td>Median of the percentage growth in shareholdings for each investor.</td><td>float64</td></tr><tr><td>totalvalue_growth_median</td><td>Median of the percentage growth in total value for each investor.</td><td>float64</td></tr><tr><td>put_call_ratio_fund_growth_median</td><td>Median of the percentage growth in put-call ratio for each investor.</td><td>float64</td></tr><tr><td>derivative_ratio_fund_growth_median</td><td>Median of the percentage growth in derivative ratio for each investor.</td><td>float64</td></tr><tr><td>market_tilt_pca_median</td><td>Median of the market tilt component calculated through PCA for each investor.</td><td>float64</td></tr><tr><td>sector_tilt_pca_median</td><td>Median of the sector tilt component calculated through PCA for each investor.</td><td>float64</td></tr><tr><td>strategy_tilt_pca_median</td><td>Median of the strategy tilt component calculated through PCA for each investor.</td><td>float64</td></tr><tr><td>quantitative_tilt_pca_median</td><td>Median of the quantitative tilt component calculated through PCA for each investor.</td><td>float64</td></tr><tr><td>instrument_tilt_pca_median</td><td>Median of the instrument tilt component calculated through PCA for each investor.</td><td>float64</td></tr><tr><td>weight_variability_median</td><td>Median of the variability in weightings for each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_mean_median</td><td>Median of the mean weights of holdings in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_coff_variance_median</td><td>Median of the coefficient of variance of weights in each investor's portfolio (variability relative to mean weight).</td><td>float64</td></tr><tr><td>weight_max_median</td><td>Median of the maximum weight in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_kurtosis_median</td><td>Median of the kurtosis of weights in each investor's portfolio (measure of the 'tailedness' of the distribution of weights).</td><td>float64</td></tr><tr><td>weight_skew_median</td><td>Median of the skewness of weights in each investor's portfolio (measure of asymmetry of the distribution of weights).</td><td>float64</td></tr><tr><td>num_investments_median</td><td>Median number of investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>new_investments_median</td><td>Median ratio of new investments to total investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>divestments_median</td><td>Median ratio of divestments to total investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>new_investments_to_divestments_median</td><td>Median ratio of new investments to divestments in each investor's portfolio.</td><td>float64</td></tr><tr><td>portfolio_turnover_median</td><td>Median portfolio turnover, measuring changes in portfolio composition, for each investor.</td><td>float64</td></tr><tr><td>net_change_to_investments_median</td><td>Median of the net change to investments, indicating the net inflow or outflow, in each investor's portfolio.</td><td>float64</td></tr><tr><td>uncorrelated_percentile_median</td><td>Median of the uncorrelated percentile, indicating the degree of uncorrelation in each investor's portfolio components.</td><td>float64</td></tr><tr><td>flow_percentage_mean_median</td><td>Median of the mean flow percentage, indicating the average flow relative to the value, in each investor's portfolio.</td><td>float64</td></tr><tr><td>performance_value_mean_median</td><td>Median of the mean performance value, indicating the average value of performance, in each investor's portfolio.</td><td>float64</td></tr><tr><td>fund_return_quarter_median</td><td>Median return of funds for each investor, calculated quarterly.</td><td>float64</td></tr><tr><td>fund_flows_percent_quarter_median</td><td>Median percentage of fund flows for each investor, calculated quarterly.</td><td>float64</td></tr><tr><td>std_percentoftotal_fund_std</td><td>Standard deviation of the rolling standard deviation of 'percentoftotal' over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>std_put_call_ratio_fund_std</td><td>Standard deviation of the rolling standard deviation of the put-call ratio over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>std_derivative_ratio_fund_std</td><td>Standard deviation of the rolling standard deviation of the derivative ratio over the last 4 quarters for each investor.</td><td>float64</td></tr><tr><td>derivative_ratio_fund_std</td><td>Standard deviation of the derivative ratio for each investor.</td><td>float64</td></tr><tr><td>put_call_ratio_fund_std</td><td>Standard deviation of the put-call ratio for each investor.</td><td>float64</td></tr><tr><td>fund_ratio_fund_std</td><td>Standard deviation of the fund ratio for each investor.</td><td>float64</td></tr><tr><td>debt_ratio_fund_std</td><td>Standard deviation of the debt ratio for each investor.</td><td>float64</td></tr><tr><td>preferred_ratio_fund_std</td><td>Standard deviation of the preferred stock ratio for each investor.</td><td>float64</td></tr><tr><td>totalvalue_std</td><td>Standard deviation of the total value of holdings for each investor.</td><td>float64</td></tr><tr><td>percentoftotal_std</td><td>Standard deviation of the percentage of total holdings for each investor.</td><td>float64</td></tr><tr><td>shrholdings_growth_std</td><td>Standard deviation of the growth in the number of shareholdings for each investor.</td><td>float64</td></tr><tr><td>totalvalue_growth_std</td><td>Standard deviation of the growth in the total value of holdings for each investor.</td><td>float64</td></tr><tr><td>put_call_ratio_fund_growth_std</td><td>Standard deviation of the growth in the put-call ratio for each investor.</td><td>float64</td></tr><tr><td>derivative_ratio_fund_growth_std</td><td>Standard deviation of the growth in the derivative ratio for each investor.</td><td>float64</td></tr><tr><td>market_tilt_pca_std</td><td>Standard deviation of the market tilt principal component analysis (PCA) for each investor.</td><td>float64</td></tr><tr><td>sector_tilt_pca_std</td><td>Standard deviation of the sector tilt principal component analysis (PCA) for each investor.</td><td>float64</td></tr><tr><td>strategy_tilt_pca_std</td><td>Standard deviation of the strategy tilt principal component analysis (PCA) for each investor.</td><td>float64</td></tr><tr><td>quantitative_tilt_pca_std</td><td>Standard deviation of the quantitative tilt principal component analysis (PCA) for each investor.</td><td>float64</td></tr><tr><td>instrument_tilt_pca_std</td><td>Standard deviation of the instrument tilt principal component analysis (PCA) for each investor.</td><td>float64</td></tr><tr><td>weight_variability_std</td><td>Standard deviation of the variability of weights of holdings in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_mean_std</td><td>Standard deviation of the mean weights of holdings in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_coff_variance_std</td><td>Standard deviation of the coefficient of variance of weights in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_max_std</td><td>Standard deviation of the maximum weight in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_kurtosis_std</td><td>Standard deviation of the kurtosis of weights in each investor's portfolio.</td><td>float64</td></tr><tr><td>weight_skew_std</td><td>Standard deviation of the skewness of weights in each investor's portfolio.</td><td>float64</td></tr><tr><td>num_investments_std</td><td>Standard deviation of the number of investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>new_investments_std</td><td>Standard deviation of the ratio of new investments to total investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>divestments_std</td><td>Standard deviation of the ratio of divestments to total investments in each investor's portfolio.</td><td>float64</td></tr><tr><td>new_investments_to_divestments_std</td><td>Standard deviation of the ratio of new investments to divestments in each investor's portfolio.</td><td>float64</td></tr><tr><td>portfolio_turnover_std</td><td>Standard deviation of portfolio turnover, measuring changes in portfolio composition, for each investor.</td><td>float64</td></tr><tr><td>net_change_to_investments_std</td><td>Standard deviation of the net change to investments, indicating the net inflow or outflow, in each investor's portfolio.</td><td>float64</td></tr><tr><td>uncorrelated_percentile_std</td><td>Standard deviation of the uncorrelated percentile, indicating the degree of uncorrelation in each investor's portfolio components.</td><td>float64</td></tr><tr><td>flow_percentage_mean_std</td><td>Standard deviation of the mean flow percentage, indicating the average flow relative to the value, in each investor's portfolio.</td><td>float64</td></tr><tr><td>performance_value_mean_std</td><td>Standard deviation of the mean performance value, indicating the average value of performance, in each investor's portfolio.</td><td>float64</td></tr><tr><td>fund_return_quarter_std</td><td>Standard deviation of quarterly fund returns for each investor.</td><td>float64</td></tr><tr><td>fund_flows_percent_quarter_std</td><td>Standard deviation of quarterly fund flows percentage for each investor.</td><td>float64</td></tr><tr><td>totalvalue</td><td>Total value of holdings for each investor.</td><td>float64</td></tr><tr><td>total_derivatives</td><td>Total value of derivative holdings (puts and calls) for each investor.</td><td>float64</td></tr><tr><td>percentoftotal</td><td>Percentage of total holdings for each investor.</td><td>float64</td></tr><tr><td>growth_totalvalue</td><td>Growth rate of the total value of holdings for each investor.</td><td>float64</td></tr><tr><td>growth_shrholders</td><td>Growth rate of the number of shareholders for each investor.</td><td>float64</td></tr><tr><td>growth_shrvalue</td><td>Growth rate of the share value for each investor.</td><td>float64</td></tr><tr><td>growth_percentoftotal</td><td>Growth rate of the percentage of total holdings for each investor.</td><td>float64</td></tr><tr><td>growth_shrholder_value_divergence</td><td>Divergence between growth rates of share value and shareholders for each investor.</td><td>float64</td></tr><tr><td>diversification_score_ticker</td><td>Score indicating the level of diversification in the portfolio based on the presence of different types of investments.</td><td>float64</td></tr><tr><td>derivative_ratio_ticker</td><td>Ratio of derivative holdings to share value for each ticker.</td><td>float64</td></tr><tr><td>derivative_holder_ratio</td><td>Ratio of derivative holders to total shareholders for each ticker.</td><td>float64</td></tr><tr><td>derivative_holder_value_divergence</td><td>Divergence between derivative holder ratio and derivative ratio for each ticker.</td><td>float64</td></tr><tr><td>short_interest</td><td>Value of short interest (put value minus share value) for each ticker.</td><td>float64</td></tr><tr><td>security_concentration</td><td>Concentration of security, calculated as share value divided by total value, for each ticker.</td><td>float64</td></tr><tr><td>put_call_ratio_ticker</td><td>Put-call ratio for each ticker, calculated as the difference between put and call values divided by their sum.</td><td>float64</td></tr><tr><td>put_call_holder_ratio</td><td>Put-call holder ratio for each ticker, calculated as the difference between put and call holders divided by their sum.</td><td>float64</td></tr><tr><td>put_holder_value_sentiment_divergence</td><td>Divergence between put-call holder ratio and put-call ratio, indicating sentiment divergence for each ticker.</td><td>float64</td></tr><tr><td>value_per_holder</td><td>Average value per holder for each ticker.</td><td>float64</td></tr><tr><td>debt_equity_ratio</td><td>Ratio of debt value to equity value for each ticker.</td><td>float64</td></tr><tr><td>historical_high_sharevalue</td><td>Historical highest share value for each ticker.</td><td>float64</td></tr><tr><td>percentage_from_high_sharevalue</td><td>Percentage difference from historical high share value for each ticker.</td><td>float64</td></tr><tr><td>previous_high_sharevalue</td><td>Previous highest share value for each ticker.</td><td>float64</td></tr><tr><td>percentage_above_previous_high</td><td>Percentage above the previous highest share value for each ticker.</td><td>float64</td></tr><tr><td>overweight</td><td>Indicator of overweight investment in a particular ticker.</td><td>float64</td></tr><tr><td>allocation_pressure_percentile</td><td>Percentile rank of allocation pressure for each ticker, indicating the degree of pressure on allocation.</td><td>float64</td></tr><tr><td>net_flows_sum</td><td>Sum of net flows for each ticker over the given period.</td><td>float64</td></tr><tr><td>net_flows_max</td><td>Maximum net flow for each ticker over the given period.</td><td>float64</td></tr><tr><td>net_flows_std</td><td>Standard deviation of net flows for each ticker over the given period.</td><td>float64</td></tr><tr><td>net_flows_mean</td><td>Mean of net flows for each ticker over the given period.</td><td>float64</td></tr><tr><td>net_flows_inflow_outflow_value_ratio</td><td>Ratio of inflows to outflows in terms of value for each ticker.</td><td>float64</td></tr><tr><td>net_flows_inflow_outflow_count_ratio</td><td>Ratio of the number of inflows to outflows for each ticker.</td><td>float64</td></tr><tr><td>appreciation_value_sum</td><td>Sum of appreciation value for each ticker over the given period.</td><td>float64</td></tr><tr><td>new_value_sum</td><td>Sum of new value for each ticker over the given period.</td><td>float64</td></tr><tr><td>turnover_percentage_median</td><td>Median of turnover percentage for each ticker over the given period.</td><td>float64</td></tr><tr><td>quarter_return</td><td>Return for each ticker in the quarter.</td><td>float64</td></tr><tr><td>quarter_flows</td><td>Flows for each ticker in the quarter.</td><td>float64</td></tr><tr><td>derivative_overloaded</td><td>Indicator of high derivative concentration for each ticker.</td><td>float64</td></tr><tr><td>put_overloaded</td><td>Indicator of high put option concentration for each ticker.</td><td>float64</td></tr></tbody></table>

## Institutional Investment Analysis

This dataset provides a comprehensive analysis of institutional investment behaviors, strategies, and portfolio dynamics. It covers various aspects like fund ratios, growth metrics, derivative concentrations, shareholder dynamics, and more. The data is designed to assist professional investors in understanding market trends, evaluating investment strategies, and making informed decisions.

### Data Applications

* **Market Trend Analysis:** Understand broad market trends by analyzing growth metrics and standard deviations.
* **Risk Assessment:** Evaluate the risk profiles of different funds and strategies using volatility and diversification metrics.
* **Strategy Evaluation:** Assess and compare the effectiveness of different investment strategies.
* **Investment Decision Making:** Utilize historical data and flow metrics to make informed investment decisions.

### Feature Descriptions

1. **Standard Deviation Metrics (Columns 0-38)**
   * **Purpose:** These metrics provide insights into the volatility and risk associated with various investment strategies and portfolio compositions.
   * **Usage:** Investors can use these metrics to assess the risk profile of different funds and compare the stability of their investment strategies.
2. **Growth Metrics (Columns 75-79)**
   * **Purpose:** These metrics track the growth or decline in the value of investments, the number of shareholders, and their share value over time.
   * **Usage:** Useful for identifying trends in investment preferences and shareholder behaviors.
3. **Diversification Score (Column 80)**
   * **Purpose:** Indicates the level of diversification in a portfolio based on different types of investments.
   * **Usage:** Investors can evaluate the risk mitigation strategies of different funds based on their diversification scores.
4. **Derivative and Put-Call Metrics (Columns 81-88)**
   * **Purpose:** Provide insights into the use of derivatives and options in investment strategies.
   * **Usage:** These metrics help in understanding the risk appetite and hedging strategies of investors.
5. **Historical Highs and Debt-Equity Ratio (Columns 90-94)**
   * **Purpose:** Offers a historical perspective on share values and assesses the leverage used by funds.
   * **Usage:** Useful for long-term investment analysis and understanding the use of debt in investment strategies.
6. **Allocation Pressure and Flow Metrics (Columns 96-107)**
   * **Purpose:** These metrics assess the inflows and outflows from funds, alongside the allocation pressure on investments.
   * **Usage:** Essential for understanding market liquidity, investor sentiment, and pressure on asset allocation.
7. **Overloaded Indicators (Columns 108-109)**
   * **Purpose:** Indicate high concentrations in derivatives and puts.
   * **Usage:** Investors can gauge the level of speculation and potential overexposure to certain investment instruments.

###

***
