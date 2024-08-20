---
description: >-
  A financial factor dataset for in-depth company analysis and investment
  strategies.
icon: wave-square
---

# Factor Signals

{% hint style="info" %}
Data is updated weekly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Factor Signals Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Factor%20Model.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Filings, Financial Data</td></tr><tr><td><strong>Models Used</strong></td><td>OLS Regression</td></tr><tr><td><strong>Model Outputs</strong></td><td>Factors, Coefficients, Standard Errors</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

***

### Financial Factors Data Documentation

This section covers the usage of various financial factors datasets. Each dataset can be accessed using the `sov.data` function from our data library.

#### Comprehensive Factors

Comprehensive Factors dataset is a merged set of both accounting and alternative financial metrics, providing a holistic view of a company's financial status.

```python
df_factor_comp = sov.data("factors/comprehensive")
```

<figure><img src="../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>

#### Accounting Factors

The Accounting Factors dataset includes key financial metrics related to accounting for various companies.

```python
df_factor_actn = sov.data("factors/accounting")
```

#### Alternative Factors

This dataset contains alternative financial factors that are not typically found in standard financial statements.

```python
df_factor_alt = sov.data("factors/alternative")
```

#### Coefficients Factors

The Coefficients Factors dataset includes various coefficients related to different financial metrics.

```python
df_factor_coeff = sov.data("factors/coefficients")
```

#### Standard Errors Factors

This dataset provides standard errors for various financial metrics, useful for statistical analysis and modeling.

```python
df_factor_std_err = get_data("factors/standard_errors")
```

#### T-Statistics Factors

The T-Statistics Factors dataset includes t-statistics for different financial metrics, offering insights into their significance.

```python
df_factor_t_stat = get_data("factors/t_statistics")
```

#### Model Metrics

Model Metrics dataset includes various metrics such as R-squared, AIC, BIC, etc., that are crucial for evaluating the performance of financial models.

```python
df_model_metrics = sov.data("factors/model_metrics")
```

#### Accessing Specific Tickers

You can also retrieve data for specific tickers across these datasets. For example:

```python
df_ticker_factors_accounting = sov.data("factors/accounting", tickers=[ "GOOGL"])
```

***

This documentation provides a clear guide on how to access each dataset, and can be easily extended or modified as needed for additional datasets or details.

## Data Dictionary

### Financial Factors Dataset

<table><thead><tr><th width="286">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>ticker</code></td><td>The unique identifier for a publicly traded company's stock.</td></tr><tr><td><code>date</code></td><td>The specific date for which the data is recorded.</td></tr><tr><td><code>profitability</code></td><td>A measure of a company's efficiency in generating profits.</td></tr><tr><td><code>value</code></td><td>Indicates the company's market value, often reflecting its perceived worth.</td></tr><tr><td><code>solvency</code></td><td>Reflects the company's ability to meet its long-term financial obligations.</td></tr><tr><td><code>cash_flow</code></td><td>Represents the amount of cash being transferred into and out of a business.</td></tr><tr><td><code>illiquidity</code></td><td>Measures the difficulty of converting assets into cash quickly without significant loss in value.</td></tr><tr><td><code>momentum_long_term</code></td><td>Indicates long-term trends in the company's stock price movements.</td></tr><tr><td><code>momentum_medium_term</code></td><td>Represents medium-term trends in stock price movements.</td></tr><tr><td><code>short_term_reversal</code></td><td>Reflects short-term price reversals in the stock market.</td></tr><tr><td><code>price_volatility</code></td><td>Measures the degree of variation in a company's stock price over time.</td></tr><tr><td><code>dividend_yield</code></td><td>The dividend per share, divided by the price per share, showing how much a company pays out in dividends each year relative to its stock price.</td></tr><tr><td><code>earnings_consistency</code></td><td>Indicates the stability and predictability of a company's earnings over time.</td></tr><tr><td><code>small_size</code></td><td>A factor indicating the company's size, with smaller companies potentially offering higher returns (albeit with higher risk).</td></tr><tr><td><code>low_growth</code></td><td>Reflects the company's lower-than-average growth prospects.</td></tr><tr><td><code>low_equity_issuance</code></td><td>Indicates a lower level of issuing new shares, which can be a sign of financial strength or limited growth prospects.</td></tr><tr><td><code>bounce_dip</code></td><td>Measures the tendency of a stock to recover quickly after a significant drop.</td></tr><tr><td><code>accrual_growth</code></td><td>Represents the growth rate in accruals, which are earnings not yet realized in cash.</td></tr><tr><td><code>low_depreciation_growth</code></td><td>Indicates lower growth in depreciation expenses, which might suggest more stable capital expenditures.</td></tr><tr><td><code>current_liquidity</code></td><td>A measure of a company's ability to pay off its short-term liabilities with its short-term assets.</td></tr><tr><td><code>low_rnd</code></td><td>Reflects lower expenditures on research and development, which could indicate less investment in future growth.</td></tr><tr><td><code>momentum</code></td><td>Overall momentum factor, representing the general trend in the stock price movements.</td></tr><tr><td><code>market_risk</code></td><td>Indicates the risk of an investment in a particular market relative to the entire market.</td></tr><tr><td><code>business_risk</code></td><td>Reflects the inherent risk associated with the specific business activities of a company.</td></tr><tr><td><code>political_risk</code></td><td>Measures the potential for losses due to political instability or changes in a country's political environment.</td></tr><tr><td><code>inflation_fluctuation</code></td><td>Indicates how sensitive the company is to fluctuations in inflation rates.</td></tr><tr><td><code>inflation_persistence</code></td><td>Measures the company's exposure to persistent inflation trends.</td></tr><tr><td><code>returns</code></td><td>Represents the financial returns generated by the company over a specified period.</td></tr></tbody></table>

### ModelMetrics Dataset

<table><thead><tr><th width="267">Name</th><th>Description</th></tr></thead><tbody><tr><td><code>ticker</code></td><td>The unique stock ticker symbol identifying the company.</td></tr><tr><td><code>date</code></td><td>The date for which the model metrics are calculated.</td></tr><tr><td><code>rsquared</code></td><td>The R-squared value, indicating the proportion of variance in the dependent variable that's predictable from the independent variables.</td></tr><tr><td><code>rsquared_adj</code></td><td>The adjusted R-squared value, accounting for the number of predictors in the model (provides a more accurate measure when dealing with multiple predictors).</td></tr><tr><td><code>fvalue</code></td><td>The F-statistic value, used to determine if the overall regression model is a good fit for the data.</td></tr><tr><td><code>aic</code></td><td>Akaike’s Information Criterion, a measure of the relative quality of statistical models for a given set of data. Lower AIC indicates a better model.</td></tr><tr><td><code>bic</code></td><td>Bayesian Information Criterion, similar to AIC but with a higher penalty for models with more parameters.</td></tr><tr><td><code>mse_resid</code></td><td>Mean Squared Error of the residuals, measuring the average of the squares of the errors, i.e., the average squared difference between the estimated values and the actual value.</td></tr><tr><td><code>mse_total</code></td><td>Total Mean Squared Error, measuring the total variance in the observed data.</td></tr></tbody></table>

In addition to the primary financial metrics and model metrics, our data suite includes three specialized datasets:

* **Coefficients**: This dataset provides regression coefficients for various financial factors. These coefficients offer insights into the relative importance and impact of each factor in financial models.
* **Standard Errors**: Accompanying the coefficients, this dataset provides the standard error for each coefficient. The standard errors are crucial for understanding the precision and reliability of the coefficients in the model.
* **T-Statistics**: This dataset contains the t-statistic for each coefficient, a key metric for determining the statistical significance of each financial factor. It helps in evaluating the robustness of the coefficients' impact in the model.

These datasets form a comprehensive toolkit for financial analysis, enabling detailed regression analysis and statistical evaluation of financial factors.

## Factor Analysis Datasets

Our suite of Factor Analysis datasets offers a rich and comprehensive resource for investors seeking to deepen their understanding of market dynamics and enhance their investment strategies. Here's an overview of each dataset and its potential use cases:

#### Comprehensive Financial Metrics

1. **Accounting Factors (`FactorsAccounting`)**: This dataset includes core financial metrics like profitability, solvency, and cash flow. It's invaluable for fundamental analysis, enabling investors to assess a company's financial health and operational efficiency.
2. **Alternative Factors (`FactorsAlternative`)**: Focusing on non-traditional financial metrics such as market risk, business risk, and political risk, this dataset helps in evaluating external factors that could impact a company's performance.
3. **Comprehensive Factors (`FactorsComprehensive`)**: A merged set of accounting and alternative factors providing a holistic view of a company's status. This dataset is perfect for a comprehensive financial analysis, blending traditional and modern financial metrics.

#### Advanced Statistical Analysis

1. **Coefficients (`FactorsCoefficients`)**: Reveals the weight or importance of each financial factor in a statistical model. Investors can use this to identify which factors are most influential in predicting stock performance.
2. **Standard Errors (`FactorsStandardErrors`)**: Provides precision levels of the coefficients. This is crucial for investors in assessing the reliability of the coefficients in predictive models.
3. **T-Statistics (`FactorsTStatistics`)**: Offers insights into the statistical significance of each factor. Investors can use this to gauge the robustness and credibility of the factors in their investment models.
4. **Model Metrics (`ModelMetrics`)**: Includes advanced metrics like R-squared, AIC, and BIC. This dataset is essential for evaluating the effectiveness of financial models, helping investors to choose the most reliable models for their investment decisions.

#### Potential Use Cases

* **Portfolio Construction and Optimization**: By understanding the importance and impact of various financial factors, investors can construct and optimize their portfolios to maximize returns and minimize risks.
* **Risk Assessment and Management**: Alternative factors, along with risk-related metrics from other datasets, enable investors to conduct thorough risk assessments, leading to better risk management strategies.
* **Market Trend Analysis**: Long-term and medium-term momentum factors can be used for identifying prevailing market trends, aiding in strategic investment decisions.
* **Statistical Model Validation**: Investors can validate their financial models using model metrics and statistical datasets (Standard Errors and T-Statistics), ensuring robustness and reliability in their analysis.

###

***
