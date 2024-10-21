---
icon: wikipedia-w
description: >-
  A look at some of the largest firms and their daily wikipedia page views and
  trends.
---

# Wikipedia Views

{% hint style="info" %}
Data is updated quarterly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Wikipedia Views Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Wikipedia.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Wikipedia Scrapers</td></tr><tr><td><strong>Models Used</strong></td><td>Fuzzy Matching</td></tr><tr><td><strong>Model Outputs</strong></td><td>Views and Trends</td></tr></tbody></table>

## Description

This dataset provides daily Wikipedia page view data and trends for major companies, offering insights into public interest and market sentiment.&#x20;

It includes metrics on view counts, relative views, and derived alpha/beta proxies to help investors gauge short-term and long-term trends in public attention towards specific stocks.

## Data Access

#### Latest Data

```python
from sovai import sov
df_news = sov.data("wikipedia/views")
```

#### All Data

This data is around 1GB if you download the entire dataset.

```python
from sovai import sov
df_news = sov.data("wikipedia/views", full_history=True)
```

<figure><img src="../../.gitbook/assets/image (30).png" alt=""><figcaption></figcaption></figure>

#### Filtered Dataset

```python
from sovai import sov
df_news = sov.data("wikipedia/views", start_date="2017-03-30", tickers=["MSFT","TSLA"])
```

## Data Dictionary

Sure, let's update the markdown table with a more precise description of each feature, incorporating the detailed understanding of how alpha and beta proxies are calculated:

***

<table><thead><tr><th width="176">Feature Name</th><th width="371">Description</th><th width="95">Type</th><th>Example</th></tr></thead><tbody><tr><td>views</td><td>The total number of page views for a specific ticker on a given date.</td><td>Float</td><td>0.992128</td></tr><tr><td>relative_views</td><td>The relative number of page views for a ticker, normalized against views on other dates or other tickers.</td><td>Float</td><td>0.992128</td></tr><tr><td>alpha_short</td><td>Short-term alpha proxy representing the change in the Exponential Moving Average (EMA) of page views over a short period. It indicates the short-term momentum or trend.</td><td>Float</td><td>0.443640</td></tr><tr><td>beta_short</td><td>Short-term beta proxy measuring the deviation of actual page views from their short-term EMA. It represents the short-term volatility or variability in interest.</td><td>Float</td><td>0.456864</td></tr><tr><td>alpha_long</td><td>Long-term alpha proxy similar to alpha_short but calculated over a longer time frame. It reflects the long-term trend or momentum in page views.</td><td>Float</td><td>0.482683</td></tr><tr><td>beta_long</td><td>Long-term beta proxy indicating the deviation of actual page views from their long-term EMA. It measures the long-term volatility or variation in attention.</td><td>Float</td><td>0.480479</td></tr><tr><td>long_short_alpha</td><td>The difference between long-term and short-term alpha proxies, highlighting the change in trend strength over varying time frames.</td><td>Float</td><td>0.627361</td></tr><tr><td>long_short_beta</td><td>The difference between long-term and short-term beta proxies, showing the change in volatility or variability over different time periods.</td><td>Float</td><td>0.683407</td></tr><tr><td>search_pressure</td><td>A composite metric calculated from a combination of alpha and beta proxies over different time frames, designed to provide a holistic view of the changing interest in a ticker.</td><td>Float</td><td>0.508743</td></tr></tbody></table>

***

This table offers a succinct yet comprehensive overview of each feature, tailored to facilitate a clear understanding of the data's dimensions and their relevance in financial analysis, especially in the context of assessing public interest and market sentiment toward different financial entities.

## Use Cases

This dataset is designed to provide investors with a detailed analysis of market interest and sentiment towards various financial entities, as reflected in Wikipedia page views. By analyzing page view trends and volatility, investors can gain insights into public interest and market sentiment, which are crucial factors in investment decision-making.

This dataset can be leveraged by investors for various purposes:

* **Market Sentiment Analysis:** By analyzing trends and volatility in page views, investors can gauge public interest and sentiment towards specific tickers.
* **Investment Decision Support:** Insights from the dataset can support buy, hold, or sell decisions based on the perceived interest and sentiment dynamics.
* **Risk Assessment:** Variability in page views, as indicated by beta proxies, can aid in assessing the market's perception of risk associated with certain tickers.
* **Trend Identification:** Alpha proxies provide a means to identify emerging trends in investor interest, which can be precursors to market movements.
* **Comparative Analysis:** Comparing alpha and beta metrics across different tickers can help identify outperformers or underperformers in terms of market interest.



***
