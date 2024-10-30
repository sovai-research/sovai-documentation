---
description: >-
  From filings we collect and match trades in the Senate and House and make them
  available within a day of processing.
icon: users-between-lines
---

# Congressional Data

{% hint style="info" %}
Data arrives daily or as new trades are being made triggering the processing of the data.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Congressional Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Congressional%20Trading.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>House and Senator Filings</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Regex</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Rows</td></tr></tbody></table>

## Description

The Congressional Trading dataset offers comprehensive insights into the financial transactions of U.S. Congress members, encompassing both Senate and House representatives. This dataset includes detailed information on securities traded, transaction dates, types of transactions (e.g., purchases, sales), transaction amounts, political party affiliations, and pertinent biographical details of each legislator.&#x20;

By providing transparency into the investment activities of elected officials, this data serves as a crucial tool for constituents, analysts, investors, and policymakers to monitor potential conflicts of interest, assess ethical compliance, and understand the financial behaviors of those in power.

## Data Access

The easiest is to just download the dump and to filter data from there, this is updated on a daily basis.

```python
from sovai import sov
df_congress = sov.data("congress")
```

<figure><img src="../../.gitbook/assets/image (151).png" alt=""><figcaption></figcaption></figure>

## Data Dictionary

| **Name**           | **Description**                                   | **Type** | **Example**                                        |
| ------------------ | ------------------------------------------------- | -------- | -------------------------------------------------- |
| `ticker`           | Stock ticker symbol traded by the representative  | object   | `AAPL`                                             |
| `date`             | Date the transaction was reported                 | object   | `2024-09-16`                                       |
| `representative`   | Name of the congressional representative          | object   | `A. Mitchell Jr. McConnell`                        |
| `bio_guide_id`     | Biographical identifier for the representative    | object   | `M000355`                                          |
| `transaction_date` | Date when the transaction occurred                | object   | `2024-09-01`                                       |
| `transaction`      | Type of transaction (e.g., Purchase, Sale)        | object   | `Purchase`                                         |
| `house`            | Congressional house affiliation (Senate or House) | object   | `Senate`                                           |
| `amount`           | Amount of the transaction in USD                  | float64  | `1001.0`                                           |
| `party`            | Political party affiliation of the representative | object   | `R` (Republican)                                   |
| `last_modified`    | Date the record was last updated                  | object   | `2024-09-16`                                       |
| `days_to_report`   | Number of days taken to report the transaction    | int64    | `15`                                               |
| `bio_guide_url`    | URL to the representative's biographical page     | object   | `https://bioguide.congress.gov/search/bio/M000355` |

***

***

## Use Cases

1. Investment Signal Generation: Utilize trading activities of congressional members to identify potential investment opportunities and market trends.
2. Insider Trading Detection: Monitor transactions by lawmakers to spot unusual trading patterns that may indicate insider information usage.
3. Sector Influence Analysis: Analyze which sectors are frequently traded by representatives to anticipate legislative support and its impact on those industries.
4. Portfolio Diversification: Incorporate insights from congressional trading data to diversify investments based on the financial behaviors of elected officials.

***
