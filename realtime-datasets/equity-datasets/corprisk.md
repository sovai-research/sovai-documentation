---
description: >-
  Here we develop three tables to develop a final score of corporate risk to US
  equities.
---

# ⭕ Risk Indicators

{% hint style="info" %}
Data arrives late Friday night 11 pm - 12 am after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — <mark style="color:blue;">`Financial Ratio Analysis`</mark>

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>SEC Filings, EDGAR API, Exchange Data.</td></tr><tr><td><strong>Models Used</strong></td><td>Transformations, Simple Maths</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Ratios</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

## Data Access

#### Accounting Risk

**Accounting Table**: This table offers a snapshot of a company’s financial status based on standard accounting metrics. It is crucial for investors to assess a company's profitability, liquidity, and solvency.

```python
from sovai import sov
df_actg_risk = sov.data("corprisk/accounting")
```

<figure><img src="../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Financial Event Risk

**Events Table**: Contains data on significant corporate events that could impact a company's financial status or investor perception. This includes mergers, acquisitions, executive changes, regulatory shifts, and other material events.

```python
from sovai import sov
df_events_risk = sov.data("corprisk/events")
```

<figure><img src="../../.gitbook/assets/image (20) (2).png" alt=""><figcaption></figcaption></figure>

#### Misstatement Risk

**Misstatement Table**: This table highlights the potential risks of financial misstatements in a company’s reporting. A higher score in this table indicates a greater risk or occurrence of financial misstatements, which can be a red flag for investors.

```python
from sovai import sov
df_miss_risk = sov.data("corprisk/misstatement")
```

<figure><img src="../../.gitbook/assets/image (21) (1).png" alt=""><figcaption></figcaption></figure>

#### Aggregated Risks

Accounting, Event, and Misstatement Risks combined together:

```python
from sovai import sov
df_miss_risk = sov.data("corprisk/risks")
```

<figure><img src="../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

## Reports

```python
from sovai import sov
sov.plot("corprisk/risks",chart_type="line")
```

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Data Dictionaries

### Financial Risks

<table><thead><tr><th width="224">Name</th><th width="304">Description</th><th width="114">Sentiment</th><th>Type</th></tr></thead><tbody><tr><td>average</td><td>The mean value of various indicators, scaled and ranked over a rolling period</td><td>Negative</td><td>float64</td></tr><tr><td>industryadjustedavg</td><td>Industry-adjusted average value</td><td>Negative</td><td>float64</td></tr><tr><td>piotroski_score</td><td>A score based on financial strength indicators from the Piotroski F-score</td><td>Positive</td><td>float64</td></tr><tr><td>altman_z_score</td><td>A score measuring a company's financial health and bankruptcy risk</td><td>Positive</td><td>float64</td></tr><tr><td>graham_number</td><td>A figure that measures a stock's fundamental value named after Benjamin Graham</td><td>Positive</td><td>float64</td></tr><tr><td>lynch_fair_value</td><td>An estimation of fair value using Peter Lynch's valuation method</td><td>Positive</td><td>float64</td></tr><tr><td>yacktman_frr</td><td>Yacktman's Forward Rate of Return, a measure of expected return</td><td>Positive</td><td>float64</td></tr><tr><td>ortiz_liquidity</td><td>A measure of asset liquidity relative to market assets</td><td>Positive</td><td>float64</td></tr><tr><td>tangibility</td><td>A ratio indicating the tangible assets held by a company</td><td>Positive</td><td>float64</td></tr><tr><td>age</td><td>The age of the company or asset in question</td><td>Positive</td><td>float64</td></tr><tr><td>oshaughnessy_1</td><td>A composite score based on value factors as per James O'Shaughnessy</td><td>Positive</td><td>float64</td></tr><tr><td>oshaughnessy_2</td><td>Another composite score following James O'Shaughnessy's methodology</td><td>Positive</td><td>float64</td></tr><tr><td>oshaughnessy_3</td><td>A third composite score by James O'Shaughnessy focusing on different factors</td><td>Negative</td><td>float64</td></tr><tr><td>beneish_m_score</td><td>A score to measure the probability of a firm manipulating its earnings</td><td>Negative</td><td>float64</td></tr><tr><td>erp5</td><td>A ranking system for stocks combining value and quality measures</td><td>Negative</td><td>float64</td></tr><tr><td>sloan_ratio</td><td>A ratio to identify earnings manipulation by comparing accruals to net income</td><td>Negative</td><td>float64</td></tr><tr><td>ohlson_score</td><td>A probability score of corporate financial distress</td><td>Negative</td><td>float64</td></tr><tr><td>dechow_equity_duration</td><td>A measure of the sustainability of a firm's earnings</td><td>Negative</td><td>float64</td></tr><tr><td>kaplan_zingales_index</td><td>An index measuring a company's financial constraints</td><td>Negative</td><td>float64</td></tr></tbody></table>

### Financial Event Risks

Some of these events are difficult to map to negative and positive sentiment, however, for calculating the average, we had to apply a mapping. Moreover, in the real table all values have been transformed into negative values.

<table><thead><tr><th width="255">Name</th><th width="269">Description</th><th>Sentiment</th><th>Type</th></tr></thead><tbody><tr><td>average</td><td>The mean value of various indicators, scaled and ranked over a rolling period</td><td>Negative</td><td>float64</td></tr><tr><td>industryadjustedavg</td><td>Industry-adjusted average value</td><td>Negative</td><td>float64</td></tr><tr><td>accountantchange</td><td>Indicator for changes in accountant</td><td>Negative</td><td>float64</td></tr><tr><td>agreementtermination</td><td>Indicator for termination of agreements</td><td>Negative</td><td>float64</td></tr><tr><td>assetacquisitioncompletion</td><td>Indicator for completion of asset acquisition</td><td>Positive</td><td>float64</td></tr><tr><td>attorneynoticereceipt</td><td>Indicator for receipt of an attorney's notice</td><td>Negative</td><td>float64</td></tr><tr><td>bankruptcy</td><td>Indicator for bankruptcy occurrences</td><td>Negative</td><td>float64</td></tr><tr><td>controlchanges</td><td>Indicator for changes in control of the registrant</td><td>Negative</td><td>float64</td></tr><tr><td>creditenhancementchange</td><td>Indicator for changes in credit enhancement or external support</td><td>Negative</td><td>float64</td></tr><tr><td>definitiveagreement</td><td>Indicator for entry into a material definitive agreement</td><td>Positive</td><td>float64</td></tr><tr><td>delistingnotice</td><td>Indicator for notice of delisting or failure to satisfy listing rules</td><td>Negative</td><td>float64</td></tr><tr><td>directorofficerchanges</td><td>Indicator for departure of directors or certain officers</td><td>Negative</td><td>float64</td></tr><tr><td>distributionfailure</td><td>Indicator for failure to make a required distribution</td><td>Negative</td><td>float64</td></tr><tr><td>ethicsamendments</td><td>Indicator for amendments to the registrant's code of ethics</td><td>Positive</td><td>float64</td></tr><tr><td>exitcosts</td><td>Indicator for costs associated with exit or disposal activities</td><td>Negative</td><td>float64</td></tr><tr><td>financialexhibits</td><td>Indicator for financial statements and exhibits</td><td>Positive</td><td>float64</td></tr><tr><td>financialobligationcreation</td><td>Indicator for creation of a direct financial obligation</td><td>Negative</td><td>float64</td></tr><tr><td>impairments</td><td>Indicator for material impairments</td><td>Negative</td><td>float64</td></tr><tr><td>incorporationamendments</td><td>Indicator for amendments to articles of incorporation or bylaws</td><td>Negative</td><td>float64</td></tr><tr><td>minesafetyreports</td><td>Indicator for mine safety reporting</td><td>Negative</td><td>float64</td></tr><tr><td>nonreliancestatement</td><td>Indicator for non-reliance on previously issued financial statements</td><td>Negative</td><td>float64</td></tr><tr><td>obligationtriggerevents</td><td>Indicator for triggering events that affect financial obligations</td><td>Negative</td><td>float64</td></tr><tr><td>operationsresults</td><td>Indicator for results of operations and financial condition</td><td>Positive</td><td>float64</td></tr><tr><td>otherevents</td><td>Indicator for other events (ambiguous context)</td><td>Negative</td><td>float64</td></tr><tr><td>regfddisclosure</td><td>Indicator for regulation FD disclosure</td><td>Positive</td><td>float64</td></tr><tr><td>schedule13dfiling</td><td>Indicator for Schedule 13D filing</td><td>Negative</td><td>float64</td></tr><tr><td>schedule13gfiling</td><td>Indicator for Schedule 13G filing</td><td>Negative</td><td>float64</td></tr><tr><td>securitiesactupdate</td><td>Indicator for Securities Act updating disclosure</td><td>Positive</td><td>float64</td></tr><tr><td>securityholdermodifications</td><td>Indicator for material modifications to rights of security holders</td><td>Positive</td><td>float64</td></tr><tr><td>servicertrusteechange</td><td>Indicator for change of servicer or trustee</td><td>Negative</td><td>float64</td></tr><tr><td>shareholdernominations</td><td>Indicator for shareholder nominations pursuant to Exchange Act Rule 14a-11</td><td>Positive</td><td>float64</td></tr><tr><td>shellstatuschange</td><td>Indicator for change in shell company status</td><td>Negative</td><td>float64</td></tr><tr><td>tenderofferstatement</td><td>Indicator for tender offer statement</td><td>Negative</td><td>float64</td></tr><tr><td>tradingsuspension</td><td>Indicator for temporary suspension of trading</td><td>Negative</td><td>float64</td></tr><tr><td>unregisteredequitysales</td><td>Indicator for unregistered sales of equity securities</td><td>Negative</td><td>float64</td></tr><tr><td>votesubmission</td><td>Indicator for submission of matters to a vote of security holders</td><td>Negative</td><td>float64</td></tr><tr><td>acquisitions</td><td>Indicator for acquisitions</td><td>Positive</td><td>float64</td></tr><tr><td>mergers</td><td>Indicator for mergers</td><td>Positive</td><td>float64</td></tr><tr><td>spinoffs</td><td>Indicator for spin-offs</td><td>Positive</td><td>float64</td></tr><tr><td>split</td><td>Indicator for splits</td><td>Positive</td><td>float64</td></tr><tr><td>tickerchange</td><td>Indicator for ticker changes</td><td>Negative</td><td>float64</td></tr></tbody></table>

### Misstatement Risks

For the misstatements, all of the variables have been changed into negative indicators, so that when the company overreports the financial health and corrects it later on, that is a negative sign.

<table><thead><tr><th width="231">Name</th><th>Description</th><th>Sentiment</th><th>Type</th></tr></thead><tbody><tr><td>average</td><td>Average misstatements accross all indicators</td><td>Negative</td><td>float64</td></tr><tr><td>industryadustedavg</td><td>Industry adjusted average</td><td>Negative</td><td>float64</td></tr><tr><td>misstatementper_neg</td><td>Misstatement percentage</td><td>Negative</td><td>float64</td></tr><tr><td>misstatementper_pos</td><td>Misstatement percentage</td><td>Positive</td><td>float64</td></tr><tr><td>cashneq</td><td>Cash and cash equivalents</td><td>Positive</td><td>float64</td></tr><tr><td>ppnenet</td><td>Property, plant, and equipment, net</td><td>Positive</td><td>float64</td></tr><tr><td>sbcomp</td><td>Stock-based compensation</td><td>Negative</td><td>float64</td></tr><tr><td>revenue</td><td>Total revenue</td><td>Positive</td><td>float64</td></tr><tr><td>retearn</td><td>Retained earnings</td><td>Positive</td><td>float64</td></tr><tr><td>payables</td><td>Accounts payable</td><td>Negative</td><td>float64</td></tr><tr><td>opinc</td><td>Operating income</td><td>Positive</td><td>float64</td></tr><tr><td>opex</td><td>Operating expenses</td><td>Negative</td><td>float64</td></tr><tr><td>netinc</td><td>Net income</td><td>Positive</td><td>float64</td></tr><tr><td>ncfo</td><td>Net cash flow from operating activities</td><td>Positive</td><td>float64</td></tr><tr><td>ncfi</td><td>Net cash flow from investing activities</td><td>Positive</td><td>float64</td></tr><tr><td>liabilitiesnc</td><td>Non-current liabilities</td><td>Negative</td><td>float64</td></tr><tr><td>liabilitiesc</td><td>Current liabilities</td><td>Negative</td><td>float64</td></tr><tr><td>intexp</td><td>Interest expense</td><td>Negative</td><td>float64</td></tr><tr><td>intangibles</td><td>Intangible assets</td><td>Positive</td><td>float64</td></tr><tr><td>fcf</td><td>Free cash flow</td><td>Positive</td><td>float64</td></tr><tr><td>ebitda</td><td>Earnings before interest, taxes, depreciation, and amortization</td><td>Positive</td><td>float64</td></tr><tr><td>depamor</td><td>Depreciation and amortization</td><td>Negative</td><td>float64</td></tr><tr><td>deferredrev</td><td>Deferred revenue</td><td>Negative</td><td>float64</td></tr><tr><td>assetsnc</td><td>Non-current assets</td><td>Positive</td><td>float64</td></tr><tr><td>assetsc</td><td>Current assets</td><td>Positive</td><td>float64</td></tr></tbody></table>

### Aggregated Risks

<table><thead><tr><th width="241">Name</th><th width="313">Description</th><th>Type</th></tr></thead><tbody><tr><td>ticker</td><td>Stock ticker symbol identifying the company</td><td>string</td></tr><tr><td>date</td><td>Date of the record</td><td>date</td></tr><tr><td>accounting</td><td>Score or value derived from accounting data</td><td>float64</td></tr><tr><td>accounting_ind_adjs</td><td>Adjusted score or value for accounting data based on industry standards</td><td>float64</td></tr><tr><td>misstatement</td><td>Score or value indicating the likelihood or extent of financial misstatements</td><td>float64</td></tr><tr><td>misstatement_ind_adjs</td><td>Adjusted score or value for misstatement data based on industry standards</td><td>float64</td></tr><tr><td>events</td><td>Score or value related to specific corporate events</td><td>float64</td></tr><tr><td>events_ind_adjs</td><td>Adjusted score or value for event data based on industry standards</td><td>float64</td></tr><tr><td>risk</td><td>Score or value indicating the level of total financial risk</td><td>float64</td></tr><tr><td>risk_ind_adjs</td><td>Adjusted score based on industry averages</td><td>float64</td></tr></tbody></table>

## Explanations

### Importance for Investors

Understanding these tables is essential for investors:

* **Risk Assessment**: By analyzing the Misstatement and its industry-adjusted tables, investors can gauge the risk associated with a company's financial reporting.
* **Comparative Analysis**: The industry-adjusted tables enable investors to compare companies within the same sector on a like-for-like basis, making the analysis more relevant and accurate.
* **Informed Decision-Making**: Comprehensive data covering raw financials and industry-adjusted scores empowers investors to make well-informed investment decisions.

***
