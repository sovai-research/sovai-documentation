---
icon: document-text
description: >-
  This section covers the usage of the ticker-mapped Patent Application and Grant dataset.
---

# Patent Data

{% hint style="info" %}
Data is updated based on patent office publication schedules (e.g., weekly for USPTO). Check source for specific update frequency.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Patent Data Tutorial`</mark>](Patent%20Data.ipynb) *<- Link to the notebook itself or a dedicated tutorial if available.*

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Patent Filings (e.g., USPTO), Company Information</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Company Name Matching/Mapping</td></tr><tr><td><strong>Model Outputs</strong></td><td>Ticker-Mapped Patent Applications, Ticker-Mapped Patent Grants</td></tr></tbody></table>

## Description

This dataset provides detailed information on patent applications and grants filed by or assigned to publicly traded companies, mapped to their respective ticker symbols. It includes textual data like titles, abstracts, descriptions, and claims, alongside metadata such as filing/grant dates, classifications (IPC, NAICS), and application/grant IDs.

This data enables analysis of corporate innovation, R&D activity, technological focus, competitive intelligence, and potential intellectual property value across different companies and sectors.

## Data Access

```python
import sovai as sov
# Ensure authentication is done if needed
# sov.token_auth(token="YOUR_TOKEN")

# Access Patent Applications
df_apps = sov.data("patents/applications", tickers=["AAPL", "AMZN"]) # Example tickers

# Access Patent Grants
df_grants = sov.data("patents/grants", tickers=["AAPL", "AMZN"]) # Example tickers
```

### Accessing Specific Tickers and Dates

You can retrieve data for specific tickers and define date ranges:

```python
# Applications for specific tickers from a start date
df_specific_apps = sov.data("patents/applications",
                            tickers=["000066.SZ", "AMZN", "AAPL"],
                            start_date="2014-11-20") # Example from notebook

# Grants for a specific ticker from a start date
df_specific_grants = sov.data("patents/grants",
                             tickers=["AMZN"],
                             start_date="2014-11-20") # Example from notebook
```

### Data Dictionaries

#### Patent Applications (`patents/applications`)

| Column Name        | Description                                                      |
| :----------------- | :--------------------------------------------------------------- |
| `ticker`           | Stock ticker symbol of the associated company                    |
| `date`             | Publication date of the patent application                       |
| `application_id`   | Unique identifier for the patent application                     |
| `org_name`         | Name of the organization listed on the application               |
| `source`           | Source category for company mapping (e.g., 'listed')             |
| `subsidiary`       | Specific subsidiary name identified (if applicable)              |
| `title`            | Title of the patent application                                  |
| `abstract`         | Abstract or summary of the patent application                    |
| `description`      | Detailed description of the invention                            |
| `claims`           | Specific claims made in the patent application                   |
| `country`          | Country code where the patent was filed (e.g., 'US')             |
| `location`         | Geographic location associated with the applicant (e.g., State)  |
| `ipc3`             | International Patent Classification (IPC) code (3-digit level)     |
| `naics`            | North American Industry Classification System (NAICS) code         |
| `app_type`         | Type of application (e.g., 'utility')                            |
| `kind`             | Kind code indicating the stage/type of publication (e.g., 'A1')  |
| `us_series_code`   | US Patent Series Code                                            |
| `claims_num`       | Number of claims in the application                              |
| `drawings_num`     | Number of drawings included in the application                   |
| `publication_id`   | Identifier for the specific publication document                 |
| `file_name`        | Source file path where the data was parsed from                  |
| `file_date`        | Original filing date of the patent application                   |

*Data based on notebook output for `df_apps`*

#### Patent Grants (`patents/grants`)

| Column Name        | Description                                                      |
| :----------------- | :--------------------------------------------------------------- |
| `ticker`           | Stock ticker symbol of the associated company                    |
| `date`             | Grant date of the patent                                         |
| `grant_id`         | Unique identifier for the granted patent                         |
| `org_name`         | Name of the organization listed on the grant (assignee)          |
| `source`           | Source category for company mapping (e.g., 'listed')             |
| `subsidiary`       | Specific subsidiary name identified (if applicable)              |
| `application_id`   | Original application ID corresponding to the grant               |
| `title`            | Title of the granted patent                                      |
| `abstract`         | Abstract or summary of the granted patent                        |
| `description`      | Detailed description of the invention                            |
| `claims`           | Specific claims allowed in the granted patent                    |
| `country`          | Country code where the patent was granted (e.g., 'US')           |
| `location`         | Geographic location associated with the assignee (e.g., State)   |
| `ipc3`             | International Patent Classification (IPC) code (3-digit level)     |
| `naics`            | North American Industry Classification System (NAICS) code         |
| `app_type`         | Type of application that led to the grant (e.g., 'utility')      |
| `kind`             | Kind code indicating the type of grant document (e.g., 'B1', 'A') |
| `us_series_code`   | US Patent Series Code                                            |
| `grant_length`     | Expected term length of the patent grant (e.g., 20 years)        |
| `claims_num`       | Number of claims allowed in the grant                            |
| `drawings_num`     | Number of drawings included in the grant publication             |
| `file_name`        | Source file path where the data was parsed from                  |
| `file_date`        | Original filing date of the application leading to the grant     |

*Data based on notebook output for `df_grants`*

## Use Cases

1.  **R&D Trend Analysis**: Track innovation trends within companies, sectors, or specific technology areas.
2.  **Competitive Intelligence**: Monitor competitors' patenting activities to understand their strategic focus and technological advancements.
3.  **Innovation Benchmarking**: Compare the volume, quality, and technological focus of patent portfolios across companies.
4.  **Technology Landscaping**: Map out key technologies and identify white spaces or crowded areas within a specific domain.
5.  **M&A Due Diligence**: Assess the intellectual property portfolio of potential acquisition targets.
6.  **Investment Analysis**: Use patent data as an indicator of a company's innovation potential and future growth prospects.
7.  **Litigation Risk Assessment**: Identify potential patent infringement risks by analyzing overlapping claims or technologies.
8.  **Identifying Key Inventors/Assignees**: Track prolific inventors or shifts in patent ownership.
9.  **Geographic Innovation Analysis**: Analyze where patent activity is concentrated geographically.
10. **Linking Patents to Products**: Understand which patents might underpin key products or services of a company.

This dataset provides a valuable resource for understanding corporate innovation landscapes and intellectual property trends.

