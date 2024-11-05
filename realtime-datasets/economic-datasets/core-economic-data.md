---
icon: apartment
description: >-
  Developed a core economic dataset that explain more than 90% of the
  variability in most economic outcomes. Forthcoming, December 2024
---

# Core Economic Data

{% hint style="info" %}
Data is updated monthly, and quarterly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Core Economic Data Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Core%20Economic%20Data.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Economic Series</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Imputation</td></tr><tr><td><strong>Model Outputs</strong></td><td>Imputed Data</td></tr></tbody></table>

## Description

This dataset provides a core set of economic indicators that explain over 90% of the variability in most economic outcomes. There are over 250 economic time series features. For there individual explanations, please see the FRED website.&#x20;

## Data Access

#### Economic Time Series

```python
from sovai import sov
df_econ = sov.data("macro/features")
```

<figure><img src="../.gitbook/assets/core_economic_data_1.png" alt=""><figcaption></figcaption></figure>

## Data Dictionary

Here we have isolated the data that describes 90% of the variance of most economic outcomes.

<table><thead><tr><th width="212">FRED Code</th><th width="422">Description</th><th>Granularity</th></tr></thead><tbody><tr><td>CLAIMSx</td><td>Initial Unemployment Claims</td><td>Monthly</td></tr><tr><td>S&#x26;P PE ratio</td><td>S&#x26;P 500 Price-Earnings Ratio</td><td>Monthly</td></tr><tr><td>gs1</td><td>1-Year Treasury Constant Maturity Rate</td><td>Monthly</td></tr><tr><td>TB6SMFFM</td><td>6-Month Treasury Bill Rate Minus Fed Funds Rate</td><td>Monthly</td></tr><tr><td>UMCSENTx</td><td>Consumer Confidence Index</td><td>Monthly</td></tr><tr><td>vxoclsx</td><td>CBOE S&#x26;P 500 Volatility Index: Close</td><td>Monthly</td></tr><tr><td>A014RE1Q156NBEA</td><td>GDP Share: Private Investment Change (%)</td><td>Quarterly</td></tr><tr><td>A823RL1Q225SBEA</td><td>Govt. Spending &#x26; Investment Change: Federal (%)</td><td>Quarterly</td></tr><tr><td>gs1tb3m</td><td>Spread Between 1-Year Treasury and 3-Month Treasury Bill</td><td>Monthly</td></tr><tr><td>cpf3mtb3m</td><td>3-Month Commercial Paper Minus 3-Month Treasury Bill</td><td>Monthly</td></tr><tr><td>DRIWCIL</td><td>Lending Willingness: Consumer Loans (%)</td><td>Quarterly</td></tr><tr><td>mrtggs10</td><td>10-Year Fixed Mortgage Rate</td><td>Monthly</td></tr><tr><td>UEMP5TO14</td><td>Unemployed for 5-14 Weeks (000s)</td><td>Monthly</td></tr><tr><td>EXUSEU</td><td>US Dollar to Euro Exchange Rate</td><td>Monthly</td></tr><tr><td>T10YFFM</td><td>10-Year Treasury Rate Minus Fed Funds Rate</td><td>Monthly</td></tr><tr><td>USEPUINDXM</td><td>US Economic Policy Uncertainty Index</td><td>Monthly</td></tr><tr><td>TLBSNNBBDIx</td><td>Business Sector Debt to Income Ratio (%)</td><td>Quarterly</td></tr><tr><td>CONSPI</td><td>Consumer Credit to Personal Income Ratio</td><td>Monthly</td></tr><tr><td>LNS14000025</td><td>Unemployment Rate: Men Over 20 (%)</td><td>Monthly</td></tr><tr><td>PERMIT</td><td>New Housing Building Permits Issued (000s)</td><td>Monthly</td></tr><tr><td>AWHMAN</td><td>Avg Weekly Hours: Manufacturing Workers</td><td>Monthly</td></tr><tr><td>S_P_div_yield</td><td>S&#x26;P 500 Dividend Yield</td><td>Monthly</td></tr><tr><td>CES1021000001</td><td>Employment in Mining &#x26; Logging (000s)</td><td>Monthly</td></tr><tr><td>HOUSTW</td><td>Housing Starts: West Region (000s Units)</td><td>Monthly</td></tr><tr><td>HOUSTNE</td><td>Housing Starts: Northeast Region (000s Units)</td><td>Monthly</td></tr><tr><td>EXCAUS</td><td>Canada / U.S. Foreign Exchange Rate</td><td>Monthly</td></tr><tr><td>HOUST</td><td>New Housing Starts (000s Units)</td><td>Monthly</td></tr><tr><td>S_P__indust</td><td>S&#x26;P 500 Industrial Sector Index</td><td>Monthly</td></tr><tr><td>MANEMP</td><td>Manufacturing Sector Employment (000s)</td><td>Monthly</td></tr><tr><td>LNS13023621</td><td>Unemployment Level: Job Losers (000s)</td><td>Monthly</td></tr></tbody></table>

You can add the series name like TB6SMFFM to the fred URL to obtain a more detailed explanation like: [https://fred.stlouisfed.org/series/TB6SMFFM](https://fred.stlouisfed.org/series/TB6SMFFM)

***
