---
description: >-
  State of the art notebook tools to designed to search, retrieve, and analyze
  financial data from the SEC's EDGAR database. This is a work-in-progress.
icon: building-lock
---

# SEC Edgar Search

`Tutorials` are the best documentation — [<mark style="color:blue;">`Edgar Filings Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/studies/Edgar%20Tools.ipynb)

## Description

This documentation outlines tools for accessing and analyzing SEC EDGAR filings data. It provides functions to search for specific filings, retrieve filing documents, extract financial statements, and visualize key financial facts.

The toolkit enables users to efficiently gather and analyze regulatory filing data for various companies, supporting in-depth financial analysis and research.

## Data Access

#### SEC Search

To search for SEC filings:

```python
import sovai as sov
sov.sec_search("CFO Resignation")
```

This function searches for filings related to the given keyword and saves the results in a CSV file. It is the fastest way to go from search query to CSV/datframe output.

* Available search parameters:
  * Search Keyword
  * CIK (Central Index Key)
  * Filing Type
  * Date Range (Start Date, End Date)
  * Company Name
  * Ticker Symbol
* Search and Download buttons functionality

<figure><img src="../../.gitbook/assets/sec_edgar_search_1 (2).png" alt=""><figcaption></figcaption></figure>

#### Loading Search Results

After performing a search, you can load the results into a pandas DataFrame:

```python
import pandas as pd
df = pd.read_csv("edgar_search_results/search_for_file_name.csv")
```

#### Accessing Specific Filings

```python
nflx_filing = sov.sec_filing("NFLX", "10-Q", "2022-06-06")
```

This creates a filing object for nflx Inc.'s 10-Q filing dated June 6, 2022.

#### Displays the full report

The filing object provides several attributes and methods for analysis:

```
nflx_filing.report
```

<figure><img src="../../.gitbook/assets/sec_edgar_search_2 (3).png" alt=""><figcaption></figcaption></figure>

#### Shows the financial statements

```python
import sovai as sov
nflx_filing = sov.sec_filing("NFLX", "10-Q", "2022-06-06")

nflx_filing.balance_sheet
nflx_filing.income_statement
nflx_filing.cash_flow_statement
```

<figure><img src="../../.gitbook/assets/sec_edgar_search_3 (2).png" alt=""><figcaption></figcaption></figure>

#### Provides sampled financial facts

Allows you to perform time-series analysis with fact-level financial data.

```
nflx_filing.sampled_facts
```

<figure><img src="../../.gitbook/assets/sec_edgar_search_4 (3).png" alt=""><figcaption></figcaption></figure>

**Generates visualizations of financial facts**

It self-selects facts that have increased/decreased the most over a lookback period that is controlled with a slider at the top, you can also add other facts from the select bar.

```
nflx_filing.plot_facts
```

<figure><img src="../../.gitbook/assets/sec_edgar_search_5 (4).png" alt=""><figcaption></figcaption></figure>
