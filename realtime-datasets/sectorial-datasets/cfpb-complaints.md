markdown
---
icon: star-sharp-half-stroke
description: >-
  This section covers a very unique dataset that tags clinical trials with their
  predicted outcome success.
---

# Clinical Trials

{% hint style="info" %}
Data is updated weekly on Fridays as is made available from regulatory filers
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Clinical Trials Tutorial`</mark>](Clinical%20Trials.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Regulatory Filings (e.g., ClinicalTrials.gov), Biochemical Data</td></tr><tr><td><strong>Models Used</strong></td><td>Deep Learning Encoders; Language Models</td></tr><tr><td><strong>Model Outputs</strong></td><td>Success prediction; Expected duration; Economic Effect</td></tr></tbody></table>

## Description

We predict the success of a clinical trial, its duration, and the expected economic impact using state-of-the-art machine learning models. Our solution leverages deep learning encoders and language models applied to regulatory filings and biochemical data. The dataset includes detailed metadata about each trial alongside predictions for regulatory phase success and/or approval rate.

This allows users to screen opportunities and anticipate outcomes with greater accuracy.

## Data Access

```python
import sovai as sov
# Ensure authentication is done if needed
# sov.token_auth(token="YOUR_TOKEN")

# Access clinical trial data including predictions
df_clinical = sov.data("clinical/trials", verbose=True, source="listed")
df_clinical.tail() # Display the last few rows
```

### Accessing Specific Tickers

You can also retrieve data for specific tickers. For example:

```python
import sovai as sov
# Note: The endpoint might vary slightly depending on API structure,
# using "clinical/trials" based on notebook examples.
# Adjust if "trials/predict" is specifically needed for ticker filtering.
df_pfizer = sov.data("clinical/trials", tickers=["PFE"], source="listed")
```

### Data Dictionary

*(Based on columns observed in `df_clinical` from the notebook**)*

| Column Name                                | Description                                                                 |
| :----------------------------------------- | :-------------------------------------------------------------------------- |
| `ticker`                                   | Stock ticker symbol of the associated company                               |
| `date`                                     | Date associated with the trial data point (e.g., latest update check)       |
| `source`                                   | Source category for company mapping (e.g., 'listed', 'foreign')           |
| `subsidiary`                               | Specific subsidiary name identified (if applicable)                         |
| `sponsor`                                  | The primary sponsor of the clinical trial                                   |
| `trial_id`                                 | Unique identifier for the clinical trial (e.g., NCT number)                 |
| `official_title`                           | The official title of the clinical study                                    |
| `sponsor_study_id`                         | Identifier assigned by the sponsor                                          |
| `brief_title`                              | A short title for the clinical study                                        |
| `lead_sponsor`                             | The primary organization responsible for the trial                          |
| `lead_sponsor_name`                        | Name of the lead sponsor                                                    |
| `sponsor_type`                             | Type of the sponsor (e.g., INDUSTRY, OTHER)                               |
| `lead_sponsor_type`                        | Type of the lead sponsor (e.g., INDUSTRY, OTHER)                          |
| `phase_category`                           | Clinical trial phase (e.g., phase_1, phase_2, phase_3, phase_4, other)    |
| `study_type`                               | Type of study (e.g., INTERVENTIONAL, OBSERVATIONAL)                       |
| `enrollment_count`                         | Target or actual number of participants enrolled                            |
| `number_of_locations`                      | Number of facilities where the trial is conducted                           |
| `healthy_volunteers`                       | Indicates if the trial accepts healthy volunteers (True/False)              |
| `enrollment_type`                          | Indicates if enrollment count is ESTIMATED or ACTUAL                        |
| `study_size_category`                      | Categorization based on enrollment count (e.g., Small, Medium, Large)     |
| `condition_keywords`                       | Keywords related to the conditions studied                                  |
| `primary_condition`                        | The main disease or condition being studied                                 |
| `intervention_type`                        | Type of intervention (e.g., DRUG, DEVICE, BIOLOGICAL)                     |
| `primary_intervention`                     | The main intervention being studied                                         |
| `intervention_name`                        | Name(s) of the intervention(s)                                              |
| `intervention_arm_group_labels`            | Labels for the different arms or groups in the study                        |
| `intervention_description`                 | Description of how the intervention is administered                         |
| `has_data_monitoring_committee`            | Indicates if a Data Monitoring Committee is overseeing the trial (True/False) |
| `responsible_party_investigator_affiliation` | Affiliation of the responsible party investigator                           |
| `responsible_party_investigator_title`     | Title of the responsible party investigator                                 |
| `responsible_party_investigator_name`      | Name of the responsible party investigator                                  |
| `first_posted_date`                        | Date the trial was first publicly posted                                    |
| `last_update_posted_date`                  | Date the trial information was last updated                                 |
| `start_date`                               | Actual or anticipated start date of the trial                               |
| `study_completion_date`                    | Actual or anticipated date the study protocol completes                     |
| `primary_completion_date`                  | Actual or anticipated date the final data for primary outcomes is collected |
| `study_locations_city`                     | Cities where the trial is conducted                                         |
| `study_locations_country`                  | Countries where the trial is conducted                                      |
| `study_locations_geopoint`                 | Geographic coordinates (latitude, longitude) of study locations           |
| `study_locations_facility`                 | Names of the facilities where the trial is conducted                        |
| `study_locations_zip`                      | ZIP/Postal codes of study locations                                         |
| `study_locations_state`                    | States/Provinces of study locations                                         |
| `standard_age_groups`                      | Age groups eligible for the trial (e.g., CHILD, ADULT, OLDER_ADULT)       |
| `sex`                                      | Eligible participant sex (e.g., ALL, MALE, FEMALE)                          |
| `minimum_age`                              | Minimum age for eligibility                                                 |
| `maximum_age`                              | Maximum age for eligibility                                                 |
| `overall_status`                           | Recruitment status of the trial (e.g., RECRUITING, COMPLETED)             |
| `status_category`                          | Categorized status (e.g., active, completed)                              |
| `status_verified_date`                     | Date the status was last verified                                           |
| `primary_outcomes_measures`                | Description of the primary outcome measures                                 |
| `primary_outcomes_timeframes`              | Time frame(s) over which primary outcomes are measured                      |
| `primary_outcomes_descriptions`            | Further details about the primary outcome measures                          |
| `secondary_outcomes_measures`              | Description of the secondary outcome measures                               |
| `secondary_outcomes_timeframes`            | Time frame(s) over which secondary outcomes are measured                    |
| `secondary_outcomes_descriptions`          | Further details about the secondary outcome measures                        |
| `has_results`                              | Indicates if results are available for the trial (True/False)               |
| `conditions`                               | List of conditions being studied                                            |
| `brief_summary`                            | A short summary of the clinical study                                       |
| `detailed_description`                     | A more detailed description of the study protocol                           |
| `masking`                                  | Type of blinding used (e.g., NONE, SINGLE, DOUBLE)                          |
| `allocation`                               | Method used to assign participants (e.g., RANDOMIZED, NA)                   |
| `intervention_model`                       | Study design model (e.g., PARALLEL, CROSSOVER, SINGLE_GROUP)              |
| `primary_purpose`                          | Main reason for the study (e.g., TREATMENT, PREVENTION, DIAGNOSTIC)       |
| `has_expanded_access`                      | Indicates if expanded access is available (True/False)                      |
| `study_duration_days`                      | Calculated duration of the study in days                                    |
| `trial_duration`                           | Duration of the trial (may be same as study_duration_days)                  |
| `references_type`                          | Type of reference provided (e.g., BACKGROUND, RESULT)                     |
| `references_citation`                      | Citations for related publications                                          |
| `references_pmid`                          | PubMed IDs for related publications                                         |
| `collaborators_name`                       | Names of collaborating organizations                                        |
| `collaborators_class`                      | Type of collaborators (e.g., INDUSTRY, OTHER)                             |
| `ipd_sharing`                              | Statement on Individual Participant Data (IPD) sharing (e.g., YES, NO)      |
| `success_prediction`                       | Model prediction score for trial success                                    |
| `economic_effect`                          | Model prediction score for potential economic impact                        |
| `duration_prediction`                      | Model prediction for the trial duration (in days)                           |
| `success_composite`                        | A composite score potentially combining success and other factors           |
| `class`                                    | Sponsor class (e.g., INDUSTRY, OTHER) - *Appears redundant with sponsor_type* |

## Use Cases

1.  **Investment Analysis**: Evaluate biotech/pharma companies based on the predicted success rate and duration of their clinical trial pipelines.
2.  **Drug Development Strategy**: Identify promising therapeutic areas or mechanisms by analyzing trials with high success predictions.
3.  **Competitive Intelligence**: Monitor competitors' trial progress, predicted success, and timelines.
4.  **Portfolio Management**: Assess the risk profile of a portfolio of clinical trials based on predicted outcomes.
5.  **Resource Allocation**: Prioritize resources towards trials with higher predicted success rates or shorter predicted durations.
6.  **Benchmarking**: Compare the predicted success rates of a company's trials against industry averages or competitors.
7.  **Market Entry Timing**: Estimate potential drug approval timelines based on predicted trial durations and success.
8.  **Identifying Undervalued Assets**: Find trials with high predicted success but potentially overlooked by the market.
9.  **Academic Research**: Study factors influencing clinical trial success using the provided predictions and metadata.
10. **Risk Mitigation**: Identify trials with low predicted success for early de-risking or partnership opportunities.

This dataset provides a powerful tool for forecasting clinical trial outcomes, aiding strategic decision-making in the pharmaceutical and biotechnology sectors.
