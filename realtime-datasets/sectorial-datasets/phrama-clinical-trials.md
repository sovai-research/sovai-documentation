---
description: >-
  This section covers a very unique dataset that tags clinical trials with their
  predicted outcome success.
icon: prescription
---

# Phrama Clinical Trials

{% hint style="info" %}
Data is updated weekly on Fridays as is made available from regulatory filers
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Clinical Trials Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Clinical%20Trials.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Regulatory Filings; Biochemical Data</td></tr><tr><td><strong>Models Used</strong></td><td>Deep Learning Encoders; Langauge Models</td></tr><tr><td><strong>Model Outputs</strong></td><td>Success prediction; Expected duration</td></tr></tbody></table>

{% hint style="success" %}
Dataset contains 850+ tickers, available from 1999-11-01 onwards.
{% endhint %}

## Description

We predict the success of a clinical trial, its duration, and the expected economic impact, including potential market reactions, using state-of-the-art machine learning models. Our solution also provides detailed metadata about each trial that allowed us to predict regulatory phase success and/or approval rate, empowering users to anticipate outcomes with greater accuracy.

Achieving an impressive 87% ROC-AUC—the highest among commercially available solutions—clients can rely on our predictions to make informed decisions. With an average of 1,052 new clinical trials launched each week, our platform lets you screen and focus on the most promising opportunities.

## Data Access

#### Prediction Data:

```python
import sovai as sov
df_clinical = sov.data("clinical/predict", full_history=True)
```

<figure><img src="../../.gitbook/assets/phrama_clinical_trials_1 (2).png" alt=""><figcaption></figcaption></figure>

#### Description Data

```python
import sovai as sov
df_clinical = sov.data("clinical/trials", full_history=True)
```

<figure><img src="../../.gitbook/assets/phrama_clinical_trials_2 (2).png" alt=""><figcaption></figcaption></figure>

### Accessing Specific Tickers

You can also retrieve data for specific tickers. For example:

```python
import sovai as sov
df_pfizer = sov.data("clinical/predict", tickers=["PFE"]) 
```

### Data Dictionary

| Column Name                     | Description                                                                |
| ------------------------------- | -------------------------------------------------------------------------- |
| ticker                          | Stock ticker symbol of the company                                         |
| date                            | Date the complaint was received                                            |
| company                         | Name of the company the complaint is against                               |
| bloomberg\_share\_id            | Bloomberg Global Share Class Level Identifier                              |
| culpability\_score              | Score indicating the company's culpability in the complaint                |
| complaint\_score                | Score based on the severity of the complaint                               |
| grievance\_score                | Score based on the grievance level of the complaint                        |
| total\_risk\_rating             | Overall risk rating combining culpability, complaint, and grievance scores |
| product                         | Financial product related to the complaint                                 |
| sub\_product                    | Specific sub-category of the financial product                             |
| issue                           | Main issue of the complaint                                                |
| sub\_issue                      | Specific sub-category of the issue                                         |
| consumer\_complaint\_narrative  | Narrative description of the complaint provided by the consumer            |
| company\_public\_response       | Public response provided by the company                                    |
| state                           | State where the complaint was filed                                        |
| zip\_code                       | ZIP code of the consumer                                                   |
| tags                            | Any tags associated with the complaint (e.g., "Servicemember")             |
| consumer\_consent\_provided     | Indicates if the consumer provided consent for sharing details             |
| submitted\_via                  | Channel through which the complaint was submitted                          |
| date\_sent\_to\_company         | Date the complaint was sent to the company                                 |
| company\_response\_to\_consumer | Type of response provided by the company to the consumer                   |
| timely\_response                | Indicates if the company responded in a timely manner                      |
| consumer\_disputed              | Indicates if the consumer disputed the company's response                  |
| selected\_name                  | Name used for company matching                                             |
| similarity                      | Similarity score for company name matching                                 |

## Use Cases

1. Risk Assessment: Evaluate the risk profile of financial institutions based on complaint data.
2. Consumer Sentiment Analysis: Analyze consumer sentiment towards different financial products and companies.
3. Regulatory Compliance: Monitor compliance issues and identify potential regulatory risks.
4. Product Performance Evaluation: Assess the performance and issues related to specific financial products.
5. Competitive Analysis: Compare complaint profiles across different financial institutions.
6. Geographic Trend Analysis: Identify regional trends in financial complaints.
7. Customer Service Improvement: Identify areas for improvement in customer service based on complaint types and resolutions.
8. ESG Research: Incorporate complaint data into Environmental, Social, and Governance (ESG) assessments.
9. Fraud Detection: Identify patterns that might indicate fraudulent activities.
10. Policy Impact Assessment: Evaluate the impact of policy changes on consumer complaints over time.

The resulting dataset provides a comprehensive view of consumer complaints in the financial sector, enabling detailed analysis of company performance, consumer issues, and regulatory compliance.
