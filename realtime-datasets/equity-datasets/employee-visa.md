---
description: >-
  The H1B dataset offers quarterly insights into foreign hiring trends, job
  details, and wages for informed decision-making.
icon: users-between-lines
---

# Employee Visa

{% hint style="info" %}
Data arrives late Friday night 11 pm - 12 as new **quarterly data** becomes available.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Employee Visa Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Employee%20Visa.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Government Data</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Regex</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Rows</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

## Data Access

#### H1B Employment data

**H1B Table**: This table offers quarterly data to track foreign hiring patterns for publicly traded companies.

```python
from sovai import sov
df_visa = sov.data("visas/h1b")
```

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Data Dictionaries

### Government Contracts

<table><thead><tr><th>Name</th><th width="314">Description</th><th width="114">Type</th><th>Example</th></tr></thead><tbody><tr><td>predicted_pay</td><td>Predicted salary for the job position</td><td>float64</td><td>190195</td></tr><tr><td>case_status</td><td>Status of the case/application</td><td>object</td><td>certified</td></tr><tr><td>case_number</td><td>Unique identifier for the case/application</td><td>object</td><td>i-203-17089-869756</td></tr><tr><td>decision_date</td><td>Date on which the decision was made</td><td>object</td><td>2017-04-06 0:00:00</td></tr><tr><td>visa_class</td><td>Type of visa applied for</td><td>object</td><td>e-3 australian</td></tr><tr><td>begin_date</td><td>Start date of employment</td><td>object</td><td>2017-07-02 0:00:00</td></tr><tr><td>end_date</td><td>End date of employment</td><td>object</td><td>2019-07-01 0:00:00</td></tr><tr><td>employer_name</td><td>Name of the employer</td><td>object</td><td>apple inc.</td></tr><tr><td>employer_address1</td><td>Address line of the employer</td><td>object</td><td>one infinite loop</td></tr><tr><td>employer_city</td><td>City where the employer is located</td><td>object</td><td>cupertino</td></tr><tr><td>employer_state</td><td>State where the employer is located</td><td>object</td><td>ca</td></tr><tr><td>employer_postal_code</td><td>Postal code of the employer</td><td>object</td><td>95014</td></tr><tr><td>soc_code</td><td>Standard Occupational Classification code</td><td>object</td><td>11-3021</td></tr><tr><td>soc_title</td><td>Title associated with the SOC code</td><td>object</td><td>computer and information systems managers</td></tr><tr><td>job_title</td><td>Title of the job</td><td>object</td><td>sw develop mgr 3</td></tr><tr><td>wage_rate_of_pay_from</td><td>Starting wage rate</td><td>float64</td><td>190195</td></tr><tr><td>wage_rate_of_pay_to</td><td>Ending wage rate</td><td>float64</td><td>190195</td></tr><tr><td>wage_unit_of_pay</td><td>Unit for the wage rate</td><td>object</td><td>year</td></tr><tr><td>full_time_position</td><td>Whether the position is full-time</td><td>object</td><td>y</td></tr><tr><td>worksite_address2</td><td>Secondary worksite address</td><td>object</td><td>None</td></tr><tr><td>worksite_state</td><td>State of the worksite</td><td>object</td><td>ca</td></tr><tr><td>prevailing_wage</td><td>Standard wage for the position</td><td>float64</td><td>190195</td></tr><tr><td>pw_unit_of_pay</td><td>Unit for the prevailing wage</td><td>object</td><td>year</td></tr><tr><td>pw_survey_name</td><td>Name of the prevailing wage survey</td><td>object</td><td>None</td></tr><tr><td>pw_other_source</td><td>Other source for prevailing wage</td><td>object</td><td>oflc online data center</td></tr><tr><td>pw_oes_year</td><td>Year of the OES prevailing wage</td><td>float64</td><td>2016</td></tr><tr><td>pw_survey_publisher</td><td>Publisher of the prevailing wage survey</td><td>object</td><td>None</td></tr><tr><td>naics_code</td><td>North American Industry Classification System code</td><td>float64</td><td>334111</td></tr><tr><td>unique_id</td><td>Unique identifier combining case number, soc_code, and employer state</td><td>object</td><td>i-203-17089-869756_11-3021_ca</td></tr><tr><td>wage_potential_increase</td><td>Potential increase in wage</td><td>float64</td><td>0</td></tr><tr><td>similarity</td><td>Similarity score</td><td>float64</td><td>1</td></tr><tr><td>bloomberg_share_id</td><td>Bloomberg's share identifier</td><td>object</td><td>BBG001S5N8V8</td></tr><tr><td>total_worker_positions</td><td>Total number of worker positions</td><td>float64</td><td>1</td></tr><tr><td>new_employment</td><td>Indicates new employment</td><td>float64</td><td>0</td></tr><tr><td>continued_employment</td><td>Indicates continued employment</td><td>float64</td><td>1</td></tr><tr><td>change_previous_employment</td><td>Indicates a change in previous employment</td><td>float64</td><td>0</td></tr><tr><td>new_concurrent_employment</td><td>Indicates new concurrent employment</td><td>float64</td><td>0</td></tr><tr><td>change_employer</td><td>Indicates a change of employer</td><td>float64</td><td>0</td></tr><tr><td>amended_petition</td><td>Indicates if there is an amended petition</td><td>float64</td><td>0</td></tr></tbody></table>

Certainly! When presenting a dataset to investors, it's crucial to create documentation that clearly explains the dataset's structure, its relevance, and potential use cases. Here's how you might structure such documentation:

***

## Dataset Overview

This dataset encompasses detailed records from labor condition applications, which are indicative of employment patterns within companies that hire foreign workers under various temporary visa categories in the United States. It provides a comprehensive view of job positions, wages, and employment periods.

### Dataset Content

The dataset includes 39 columns, each representing a specific attribute related to labor condition applications. Key attributes include:

* Case status and number, providing insight into the application's outcome and unique identification.
* Visa class, which distinguishes between different types of temporary work visas.
* Employment period, outlined by the begin and end dates of employment.
* Employer information, including name, address, city, state, and postal code.
* Job details, such as job title, Standard Occupational Classification (SOC) code and title.
* Wage information, including the rate of pay and prevailing wage details.
* Worksite information, offering location details where the employment takes place.
* Additional attributes related to the petition's nature, like new employment, continued employment, and any amendments.

### Use Cases

1. **Labor Market Analysis**: Investors can identify trends in employment such as demand for specific roles or average wages offered across sectors, informing investment strategies.
2. **Compliance Monitoring**: Companies can ensure their wage offerings are competitive and compliant with prevailing wage standards for different visa categories.
3. **Immigration Impact Assessment**: Policy analysts can evaluate the effects of visa policies on workforce composition and availability in various industries.
4. **Strategic Planning**: Businesses can plan recruitment strategies based on the availability of talent within certain visa classes and adjust their workforce accordingly.
5. **Investment Decision Making**: Investors can gauge the health and growth potential of sectors by analyzing the number of new and continuing employment positions.

***
