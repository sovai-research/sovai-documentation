---
description: >-
  Here we develop three tables to develop a final score of corporate risk to US
  equities. More than 100+ institutional trading variables.
---

# 📰 News Sentiment

{% hint style="info" %}
Data is updated quarterly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — <mark style="color:blue;">`Financial Ratio Analysis`</mark>

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>News Scrapers</td></tr><tr><td><strong>Models Used</strong></td><td>Fuzzy Matching</td></tr><tr><td><strong>Model Outputs</strong></td><td>Sentiment Scores</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

## Data Access

#### Institutional Trading Data

This data is around 1GB if you download the entire dataset.

```python
from sovai import sov
df_news = sov.data("news/daily")
```

<figure><img src="../../.gitbook/assets/image (24) (1).png" alt=""><figcaption></figcaption></figure>

#### Filtered Dataset

```python
from sovai import sov
df_news = sov.data("news/daily", start_date="2017-03-30", tickers=["MSFT","TSLA"])
```

## Data Dictionary

<table><thead><tr><th width="170">Feature Name</th><th width="364">Description</th><th width="100">Type</th><th>Example</th></tr></thead><tbody><tr><td>match_quality</td><td>Quality score of the match between the article and the entity, indicating the relevance and accuracy of the match.</td><td>float</td><td>99.75</td></tr><tr><td>within_article</td><td>Number of mentions of the entity within the article, indicating the focus on the entity in the article's content.</td><td>int</td><td>2</td></tr><tr><td>relevance</td><td>The average salience of the entity across the articles, indicating the importance or prominence of the entity.</td><td>float</td><td>0.022049</td></tr><tr><td>magnitude</td><td>A measure of the intensity or strength of the sentiment expressed in the article.</td><td>float</td><td>18.203125</td></tr><tr><td>sentiment</td><td>A score representing the overall sentiment (positive or negative) of the article.</td><td>float</td><td>0.054504</td></tr><tr><td>article_count</td><td>The total number of articles associated with the entity, indicating the level of media attention or coverage.</td><td>int</td><td>1666</td></tr><tr><td>associated_people</td><td>Count of unique people mentioned in the context of the entity, reflecting its association with various individuals.</td><td>int</td><td>143</td></tr><tr><td>associated_companies</td><td>Count of unique companies mentioned in relation to the entity, indicating its business connections.</td><td>int</td><td>287</td></tr><tr><td>tone</td><td>The overall tone of the article, derived from a textual analysis of its content.</td><td>float</td><td>0.237061</td></tr><tr><td>positive</td><td>The score quantifying the positive sentiments expressed in the article.</td><td>float</td><td>2.828125</td></tr><tr><td>negative</td><td>The score quantifying the negative sentiments expressed in the article.</td><td>float</td><td>2.591797</td></tr><tr><td>polarity</td><td>The degree of polarity in the sentiment, indicating the extent of opinionated content.</td><td>float</td><td>5.421875</td></tr><tr><td>activeness</td><td>A measure of the dynamism in the language used, possibly indicating the urgency of the article.</td><td>float</td><td>22.031250</td></tr><tr><td>pronouns</td><td>The count of pronouns used in the article, indicative of the narrative style or subject focus.</td><td>float</td><td>0.995117</td></tr><tr><td>word_count</td><td>The total number of words in the article, giving an indication of its length or detail.</td><td>int</td><td>1084</td></tr></tbody></table>

## News Sentiment

This dataset provides a comprehensive analysis of various entities (such as companies and individuals) based on their media coverage and associated articles. It's designed to assist investors in understanding the market sentiment, media focus, and the overall perception of entities in which they might be interested. The data is extracted and processed from a wide range of articles, ensuring a broad and in-depth view of each entity.

### Data Usage

This dataset is an invaluable resource for investors seeking to gauge public perception, media sentiment, and the prominence of entities in the news. It can be used for:

* Sentiment analysis to understand the market mood.
* Identifying trends in media coverage related to specific entities.
* Assessing the impact of news on stock performance.
* Conducting peer comparison based on media presence and sentiment.

###

***
