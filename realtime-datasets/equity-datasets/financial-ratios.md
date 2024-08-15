---
description: >-
  More than 80+ financial ratios calculated from financial statement and market
  data.
---

# 🟩 Financial Ratios

{% hint style="warning" %}
This dataset is replaceable with your preferred standardized ratio dataset, currently it is built from public filings with the values 95% confirmed against five commercial datasets.
{% endhint %}

{% hint style="info" %}
Data arrives late Friday night 11 pm - 12 am after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — <mark style="color:blue;">`Financial Ratio Analysis`</mark>

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>SEC Filings, EDGAR API, Exchange Data.</td></tr><tr><td><strong>Models Used</strong></td><td>Transformations, Simple Maths</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Ratios</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

### Data Access

#### Retrieving Data

Fetch the latest index data using the SDK:

```python
from sovai import sov
df_ratios = sov.data("ratios/normal")
```

<figure><img src="../../.gitbook/assets/image (15) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Retrieve a Subsection

Filter by `ticker` or `date` to select ratios:

```python
from sovai import sov
df_ratios = sov.data("ratios/normal", start_date="2008-03-30", tickers=["AMZN","MMM"])
```

#### Relative data

You can also obtain data in percentiles across time with `ratios/relative`.

```python
from sovai import sov
df_percentile = sov.data("ratios/relative", start_date="2018-01-01", tickers=["TSLA", "META"])
```

## Plots

### Benchmark Analysis

```python
import sovai as sov
sov.plot("ratios", chart_type="benchmark")
```

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Dynamic Ratios

```python
import sovai as sov
sov.plot("ratios", chart_type="relative")
```

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

###

### Data Dictionary

<table><thead><tr><th width="321">Name</th><th width="282">Description</th><th>Category</th></tr></thead><tbody><tr><td>current_ratio</td><td>Current assets divided by current liabilities</td><td>Liquidity</td></tr><tr><td>quick_ratio</td><td>(Current assets minus inventory) divided by current liabilities</td><td>Liquidity</td></tr><tr><td>cash_ratio</td><td>Cash divided by current liabilities</td><td>Liquidity</td></tr><tr><td>operating_cash_flow_ratio</td><td>Operating cash flow divided by current liabilities</td><td>Cash Flow</td></tr><tr><td>net_working_capital_ratio</td><td>(Current assets minus current liabilities) divided by total assets</td><td>Liquidity</td></tr><tr><td>acid_test_ratio</td><td>(Current assets minus inventory) divided by short-term debt</td><td>Liquidity</td></tr><tr><td>excess_cash_margin_ratio</td><td>(Operating cash flow minus operating income) divided by revenue</td><td>Profitability</td></tr><tr><td>earnings_per_share</td><td>Net income divided by weighted average shares outstanding</td><td>Profitability</td></tr><tr><td>gross_profit_margin</td><td>Gross profit divided by revenue</td><td>Profitability</td></tr><tr><td>operating_profit_margin</td><td>Operating income divided by revenue</td><td>Profitability</td></tr><tr><td>ebitda_margin</td><td>EBITDA divided by revenue</td><td>Profitability</td></tr><tr><td>net_profit_margin</td><td>Net income divided by revenue</td><td>Profitability</td></tr><tr><td>return_on_assets</td><td>Net income divided by total assets</td><td>Profitability</td></tr><tr><td>return_on_equity</td><td>Net income divided by equity</td><td>Profitability</td></tr><tr><td>return_on_net_assets</td><td>Net income divided by (net property, plant, equipment + working capital)</td><td>Profitability</td></tr><tr><td>roce_sub_cash</td><td>Operating income divided by (assets minus cash and certain liabilities)</td><td>Profitability</td></tr><tr><td>roce_with_cash</td><td>Operating income divided by (assets minus certain liabilities)</td><td>Profitability</td></tr><tr><td>fcf_roce_with_cash</td><td>Free cash flow divided by (assets minus certain liabilities)</td><td>Profitability</td></tr><tr><td>fcf_roce_sub_cash</td><td>Free cash flow divided by (assets minus cash and certain liabilities)</td><td>Profitability</td></tr><tr><td>income_dividend_payout_ratio</td><td>Dividends divided by net income</td><td>Profitability</td></tr><tr><td>return_on_invested_capital</td><td>EBIT divided by invested capital</td><td>Profitability</td></tr><tr><td>asset_turnover</td><td>Revenue divided by total assets</td><td>Efficiency</td></tr><tr><td>inventory_turnover</td><td>Cost of revenue divided by inventory</td><td>Efficiency</td></tr><tr><td>days_sales_outstanding</td><td>(Receivables divided by revenue) multiplied by 365</td><td>Efficiency</td></tr><tr><td>days_inventory_outstanding</td><td>(Inventory divided by cost of revenue) multiplied by 365</td><td>Efficiency</td></tr><tr><td>days_payable_outstanding</td><td>(Payables divided by cost of revenue) multiplied by 365</td><td>Efficiency</td></tr><tr><td>cash_conversion_cycle</td><td>Sum of days sales and inventory outstanding minus days payable outstanding</td><td>Efficiency</td></tr><tr><td>total_asset_efficiency</td><td>(Revenue divided by net property, plant, equipment) plus (revenue divided by current assets)</td><td>Efficiency</td></tr><tr><td>working_capital_turnover_ratio</td><td>Revenue divided by (current assets minus current liabilities)</td><td>Efficiency</td></tr><tr><td>gross_operating_cycle</td><td>Sum of days inventory and sales outstanding</td><td>Efficiency</td></tr><tr><td>sg_and_gross_profit_ratio</td><td>SG&#x26;A divided by gross profit</td><td>Profitability</td></tr><tr><td>depreciation_revenue_ratio</td><td>Depreciation divided by revenue</td><td>Efficiency</td></tr><tr><td>depreciation_cfo_ratio</td><td>Depreciation divided by cash flow from operations</td><td>Efficiency</td></tr><tr><td>debt_ratio</td><td>Total debt divided by total assets</td><td>Solvency</td></tr><tr><td>equity_multiplier</td><td>Total assets divided by equity</td><td>Solvency</td></tr><tr><td>interest_coverage_ratio</td><td>EBIT divided by interest expense</td><td>Solvency</td></tr><tr><td>debt_to_capital</td><td>Debt divided by (debt plus equity)</td><td>Solvency</td></tr><tr><td>debt_service_coverage</td><td>(Operating income minus CapEx) divided by interest expense</td><td>Solvency</td></tr><tr><td>liabilities_equity_ratio</td><td>Total liabilities divided by equity</td><td>Solvency</td></tr><tr><td>debt_ebitda_ratio</td><td>Total debt divided by EBITDA</td><td>Solvency</td></tr><tr><td>debt_ebitda_minus_capex_ratio</td><td>Total debt divided by (EBITDA minus CapEx)</td><td>Solvency</td></tr><tr><td>debt_equity_ratio</td><td>Total debt divided by equity</td><td>Solvency</td></tr><tr><td>ebitda_interest_coverage</td><td>EBITDA divided by interest expense</td><td>Solvency</td></tr><tr><td>ebitda_minus_capex_interest_coverage</td><td>(EBITDA minus CapEx) divided by interest expense</td><td>Solvency</td></tr><tr><td>interest_to_cfo_plus_interest_coverage</td><td>Interest expense divided by (cash flow from operations plus interest expense)</td><td>Liquidity</td></tr><tr><td>debt_to_total_capital</td><td>Total debt divided by invested capital</td><td>Solvency</td></tr><tr><td>debt_cfo_ratio</td><td>Total debt divided by cash flow from operations</td><td>Solvency</td></tr><tr><td>ltdebt_cfo_ratio</td><td>Long-term debt divided by cash flow from operations</td><td>Solvency</td></tr><tr><td>ltdebt_earnings_ratio</td><td>Long-term debt divided by net income</td><td>Solvency</td></tr><tr><td>cash_flow_to_debt_ratio</td><td>Cash flow from operations divided by total debt</td><td>Cash Flow</td></tr><tr><td>cash_flow_coverage_ratio</td><td>Cash flow from operations divided by interest expense</td><td>Cash Flow</td></tr><tr><td>operating_cash_flow_to_sales</td><td>Cash flow from operations divided by revenue</td><td>Cash Flow</td></tr><tr><td>free_cash_flow_conversion_ratio</td><td>Free cash flow divided by EBITDA</td><td>Cash Flow</td></tr><tr><td>rough_dividend_payout_ratio</td><td>Dividends divided by (net income plus depreciation)</td><td>Dividend</td></tr><tr><td>dividends_cfo_ratio</td><td>Dividends divided by cash flow from operations</td><td>Dividend</td></tr><tr><td>preferred_cfo_ratio</td><td>Preferred dividends divided by cash flow from operations</td><td>Dividend</td></tr><tr><td>cash_flow_reinvestment_ratio</td><td>(CapEx plus change in working capital) divided by cash flow from operations</td><td>Cash Flow</td></tr><tr><td>free_cashflow_ps</td><td>Free cash flow divided by weighted average shares outstanding</td><td>Cash Flow</td></tr><tr><td>price_to_earnings</td><td>Market capitalization divided by net income</td><td>Valuation</td></tr><tr><td>price_to_book</td><td>Share price divided by book value per share</td><td>Valuation</td></tr><tr><td>price_to_sales</td><td>Market capitalization divided by revenue</td><td>Valuation</td></tr><tr><td>dividend_yield</td><td>Dividends per share divided by share price</td><td>Dividend</td></tr><tr><td>market_to_book_ratio</td><td>Market capitalization divided by equity</td><td>Valuation</td></tr><tr><td>ev_opinc_ratio</td><td>Enterprise value divided by operating income</td><td>Valuation</td></tr><tr><td>rough_ffo</td><td>Net income plus depreciation</td><td>Cash Flow</td></tr><tr><td>dividend_payout_ratio_pref</td><td>Preferred dividends divided by net income</td><td>Dividend</td></tr><tr><td>dividend_payout_ratio</td><td>Dividends per share divided by earnings per share</td><td>Dividend</td></tr><tr><td>retention_ratio</td><td>1 minus the dividend payout ratio</td><td>Dividend</td></tr><tr><td>greenblatt_earnings_yield</td><td>EBIT divided by enterprise value</td><td>Valuation</td></tr><tr><td>enterprise_value_to_revenue</td><td>Enterprise value divided by revenue</td><td>Valuation</td></tr><tr><td>enterprise_value_to_ebitda</td><td>Enterprise value divided by EBITDA</td><td>Valuation</td></tr><tr><td>enterprise_value_to_ebit</td><td>Enterprise value divided by EBIT</td><td>Valuation</td></tr><tr><td>enterprise_value_to_invested_capital</td><td>Enterprise value divided by invested capital</td><td>Valuation</td></tr><tr><td>enterprise_value_to_free_cash_flow</td><td>Enterprise value divided by free cash flow</td><td>Valuation</td></tr><tr><td>cash_productivity_ratio</td><td>(Market capitalization plus non-current debt minus assets) divided by short-term cash</td><td>Efficiency</td></tr><tr><td>debt_to_market_ratio</td><td>Total debt divided by market capitalization</td><td>Solvency</td></tr><tr><td>net_debt_to_price_ratio</td><td>(Total debt minus short-term cash) divided by market capitalization</td><td>Solvency</td></tr><tr><td>cash_flow_to_price_ratio</td><td>(Operating cash flow minus CapEx) divided by market capitalization</td><td>Cash Flow</td></tr><tr><td>rd_to_market_ratio</td><td>R&#x26;D expenses divided by market capitalization</td><td>Innovation</td></tr><tr><td>book_to_market_enterprise_value_ratio</td><td>Book equity value divided by modified enterprise value</td><td>Valuation</td></tr><tr><td>equity_payout_yield</td><td>(Total dividends plus preferred dividends) divided by market capitalization</td><td>Dividend</td></tr><tr><td>equity_net_payout_yield</td><td>(Total dividends minus (net income minus preferred dividends)) divided by market capitalization</td><td>Dividend</td></tr><tr><td>ebitda_to_mev_ratio</td><td>EBITDA divided by modified enterprise value</td><td>Valuation</td></tr></tbody></table>

***
