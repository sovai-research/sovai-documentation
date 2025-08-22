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

{% hint style="success" %}
Dataset contains 850+ tickers, available from 1999-11-01 onwards.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Clinical Trials Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Clinical%20Trials.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Regulatory Filings; Biochemical Data</td></tr><tr><td><strong>Models Used</strong></td><td>Deep Learning Encoders; Langauge Models</td></tr><tr><td><strong>Model Outputs</strong></td><td>Success prediction; Expected duration</td></tr></tbody></table>

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

**Type:** sectorial (pharma/biotech)\
**Endpoints:** `clinical/predict`, `clinical/trials`\
**Frequency:** weekly updates (typical)\
**Index (often):** `ticker`, `date`

***

### `clinical/predict` — Prediction outputs

| Column               | Type   | Description                              |
| -------------------- | ------ | ---------------------------------------- |
| ticker               | string | Mapped company ticker (or source label)  |
| date                 | date   | Record/snapshot date                     |
| success\_prediction  | float  | Prob. of trial success (0–1)             |
| economic\_effect     | float  | Modeled economic impact (unitless index) |
| duration\_prediction | float  | Predicted trial duration (days)          |
| success\_composite   | float  | Composite success score (0–1)            |
| class                | string | Sponsor class (e.g., INDUSTRY/NIH/OTHER) |

**Notes**

* Values are model outputs; ranges typically 0–1 for probabilities/scores.
* `duration_prediction` is in days (e.g., 732 ≈ 2 yrs).

***

### `clinical/trials` — Trial descriptions & metadata (≈75 fields)

#### A) Source & sponsor

| Column     | Type   | Description                                           |
| ---------- | ------ | ----------------------------------------------------- |
| source     | string | Record source class (e.g., government/private/listed) |
| subsidiary | string | Sponsor subsidiary (if any)                           |
| sponsor    | string | Normalized sponsor org                                |
| class      | string | Sponsor class (e.g., INDUSTRY/NIH/OTHER)              |

#### B) Identifiers & titles

| Column             | Type   | Description                    |
| ------------------ | ------ | ------------------------------ |
| trial\_id          | string | Registry ID (e.g., NCT number) |
| sponsor\_study\_id | string | Sponsor’s internal study ID    |
| official\_title    | string | Official study title           |
| brief\_title       | string | Short study title              |

#### C) Lead sponsor

| Column              | Type   | Description                                     |
| ------------------- | ------ | ----------------------------------------------- |
| lead\_sponsor       | string | Lead sponsor label                              |
| lead\_sponsor\_name | string | Lead sponsor name                               |
| sponsor\_type       | string | Sponsor type (e.g., INDUSTRY/NIH/OTHER/NETWORK) |
| lead\_sponsor\_type | string | Lead sponsor type (same coding)                 |

#### D) Study classification

| Column                | Type   | Description                       |
| --------------------- | ------ | --------------------------------- |
| study\_type           | string | INTERVENTIONAL/OBSERVATIONAL/etc. |
| phase\_category       | string | phase\_1/2/3/other                |
| enrollment\_type      | string | ACTUAL/ESTIMATED                  |
| enrollment\_count     | int    | Planned/actual enrollment         |
| study\_size\_category | string | Small/Medium/Large/Very Large     |
| healthy\_volunteers   | bool   | Healthy volunteers included       |

#### E) Conditions & interventions

| Column                           | Type   | Description                           |
| -------------------------------- | ------ | ------------------------------------- |
| condition\_keywords              | string | Keyword list (semicolon-delimited)    |
| primary\_condition               | string | Primary condition/disease             |
| intervention\_type               | string | DRUG/BIOLOGICAL/PROCEDURE/etc. (list) |
| primary\_intervention            | string | Primary intervention label            |
| intervention\_name               | string | Intervention name(s)                  |
| intervention\_arm\_group\_labels | string | Arm/group labels                      |
| intervention\_description        | string | Brief arm/intervention description    |

#### F) Oversight & responsibility

| Column                                        | Type   | Description                 |
| --------------------------------------------- | ------ | --------------------------- |
| has\_data\_monitoring\_committee              | bool   | DMC presence                |
| responsible\_party\_investigator\_affiliation | string | RP investigator affiliation |
| responsible\_party\_investigator\_title       | string | RP investigator title       |
| responsible\_party\_investigator\_name        | string | RP investigator name        |

#### G) Key dates

| Column                     | Type | Description                 |
| -------------------------- | ---- | --------------------------- |
| first\_posted\_date        | date | First posted date           |
| last\_update\_posted\_date | date | Last posted update          |
| start\_date                | date | Study start date            |
| primary\_completion\_date  | date | Primary endpoint completion |
| study\_completion\_date    | date | Final completion date       |

#### H) Locations

| Column                     | Type   | Description                         |
| -------------------------- | ------ | ----------------------------------- |
| study\_locations\_city     | string | City list (semicolon-delimited)     |
| study\_locations\_state    | string | State/region list                   |
| study\_locations\_country  | string | Country list                        |
| study\_locations\_zip      | string | ZIP/postal list                     |
| study\_locations\_facility | string | Facility/site list                  |
| study\_locations\_geopoint | string | lat/lon pairs (semicolon-delimited) |

#### I) Eligibility

| Column                | Type   | Description              |
| --------------------- | ------ | ------------------------ |
| standard\_age\_groups | string | ADULT/OLDER\_ADULT/CHILD |
| sex                   | string | ALL/MALE/FEMALE          |
| minimum\_age          | int    | Minimum age (yrs)        |
| maximum\_age          | int    | Maximum age (yrs or NA)  |

#### J) Status

| Column                 | Type   | Description                       |
| ---------------------- | ------ | --------------------------------- |
| overall\_status        | string | RECRUITING/COMPLETED/etc.         |
| status\_category       | string | Active/completed/terminated, etc. |
| status\_verified\_date | date   | Status verified date              |

#### K) Outcomes — primary

| Column                          | Type   | Description            |
| ------------------------------- | ------ | ---------------------- |
| primary\_outcomes\_measures     | string | Primary measure(s)     |
| primary\_outcomes\_timeframes   | string | Timeframe(s)           |
| primary\_outcomes\_descriptions | string | Measure description(s) |

#### L) Outcomes — secondary

| Column                            | Type   | Description          |
| --------------------------------- | ------ | -------------------- |
| secondary\_outcomes\_measures     | string | Secondary measure(s) |
| secondary\_outcomes\_timeframes   | string | Timeframe(s)         |
| secondary\_outcomes\_descriptions | string | Description(s)       |

#### M) Results & narrative

| Column                | Type   | Description          |
| --------------------- | ------ | -------------------- |
| has\_results          | bool   | Results posted flag  |
| conditions            | string | Condition list       |
| brief\_summary        | string | Short summary        |
| detailed\_description | string | Detailed description |

#### N) Design

| Column                | Type   | Description                   |
| --------------------- | ------ | ----------------------------- |
| masking               | string | NONE/SINGLE/DOUBLE            |
| allocation            | string | RANDOMIZED/NON\_RANDOMIZED/NA |
| intervention\_model   | string | PARALLEL/SINGLE\_GROUP/etc.   |
| primary\_purpose      | string | TREATMENT/PREVENTION/etc.     |
| has\_expanded\_access | bool   | Expanded access flag          |

#### O) Duration & references

| Column                | Type   | Description                    |
| --------------------- | ------ | ------------------------------ |
| study\_duration\_days | int    | Duration (days)                |
| trial\_duration       | float  | Duration (days, numeric)       |
| references\_type      | string | BACKGROUND/RESULT/DERIVED/etc. |
| references\_citation  | string | Pub citations                  |
| references\_pmid      | string | PMIDs (semicolon-delimited)    |

#### P) Collaborators & sharing

| Column               | Type   | Description                  |
| -------------------- | ------ | ---------------------------- |
| collaborators\_name  | string | Collaborator names           |
| collaborators\_class | string | NIH/INDUSTRY/OTHER\_GOV/etc. |
| ipd\_sharing         | string | YES/NO/UNKNOWN               |

#### Q) Model outputs (on trials table)

| Column               | Type  | Description                   |
| -------------------- | ----- | ----------------------------- |
| success\_prediction  | float | Prob. of success (0–1)        |
| economic\_effect     | float | Modeled economic impact index |
| duration\_prediction | float | Predicted duration (days)     |
| success\_composite   | float | Composite success score       |

#### R) Index (often present as index columns)

| Column | Type   | Description                                                            |
| ------ | ------ | ---------------------------------------------------------------------- |
| ticker | string | Mapped company ticker (public) or source label (e.g., GOV/PRIVATE/SGP) |
| date   | date   | Record/snapshot date                                                   |

**Common derivations**

* `links` (derived): `https://clinicaltrials.gov/study/` + `trial_id`
* Location fields often contain semicolon-separated lists.

***

#### Want this appended to your Excel?

Say the word and I’ll append both `clinical/predict` and `clinical/trials` dictionaries to the spreadsheet I already made for you and share an updated file.

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
