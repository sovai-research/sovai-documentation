---
description: >-
  The government spending data provides comprehensive information about
  government contracts, transactions, product specifications, entity details,
  locations, competition, and compensation.
---

# 🏗️ Government Contracts

{% hint style="info" %}
Data arrives late Friday night 11 pm - 12 am after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Government Contracts Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Government%20Spending.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>SEC Filings, EDGAR API, Exchange Data.</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Regex, Entity Recognition</td></tr><tr><td><strong>Model Outputs</strong></td><td>Standardized Contracts</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

## Data Access

#### Contracts Data

Data about contract award details, potential total value, federal action obligations, performance duration, and recipient details.

```python
from sovai import sov
df_contracts = sov.data("spending/contracts", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (60).png" alt=""><figcaption></figcaption></figure>

#### Transactions Data:

The data includes information about individual transactions related to contracts, such as federal action obligations, transaction descriptions, and last modified dates.

```python
from sovai import sov
df_transactions = sov.data("spending/transactions", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (62).png" alt=""><figcaption></figcaption></figure>

#### Product Specifications

Data about the products or services associated with contracts, such as product or service code descriptions, NAICS codes and descriptions, country of origin, and sustainability information.

```python
from sovai import sov
df_product = sov.data("spending/product", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (65).png" alt=""><figcaption></figcaption></figure>

#### Entity Specification

Data about the entities involved in contracts, such as recipient unique identifiers, recipient names, parent company details, and matching information with other datasets like Bloomberg.

```python
from sovai import sov
df_entities = sov.data("spending/entities", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (67).png" alt=""><figcaption></figcaption></figure>

#### Location Data

Data about the geographical locations associated with contracts, such as recipient country, address, city, county, state, and zip code, as well as the primary place of performance details.

```python
from sovai import sov
df_location = sov.data("spending/location", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

#### Competition Data:

Data related to the competition aspect of contracts, such as the extent of competition, number of offers received, and solicitation procedures.

```python
from sovai import sov
df_competition = sov.data("spending/competition", tickers=["MSFT","TSLA"])
```

<figure><img src="../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

#### Compensation Date

Data about the compensation of highly compensated officers in recipient organization, only published voluntarily by a few companies.

```python
from sovai import sov
df_compensation = sov.data("spending/compensation")
```

<figure><img src="../../.gitbook/assets/image (22) (1).png" alt=""><figcaption></figcaption></figure>

## Data Dictionaries

### Government Contracts

<table><thead><tr><th width="258">Column Name</th><th width="268">Description</th><th>Example</th></tr></thead><tbody><tr><td>ticker</td><td>Stock ticker symbol identifying the company.</td><td>TSLA</td></tr><tr><td>date</td><td>Date of the record.</td><td>2023-10-02</td></tr><tr><td>contract_award_unique_key</td><td>Unique key identifying the prime award.</td><td>CONT_AWD_SPE7LX24F0359_9700_SPE7LX22D0144_9700</td></tr><tr><td>potential_total_value_of_award</td><td>Total amount that could be obligated on a contract if all options are exercised.</td><td>8526.629883</td></tr><tr><td>total_federal_action_obligation</td><td>Total value of federal obligations for the contract.</td><td>8526.629883</td></tr><tr><td>obligation_value_difference</td><td>Difference between the total federal action obligation and the potential total value of the award.</td><td>0.0</td></tr><tr><td>performance_duration</td><td>Duration of the contract's performance period in days.</td><td>30.0</td></tr><tr><td>awards_past_year</td><td>Count of awards per recipient name in the past year.</td><td>7.0</td></tr><tr><td>transactions_per_award</td><td>Count of unique transactions per award.</td><td>1.0</td></tr><tr><td>prime_award_base_transaction_description</td><td>Description of the transaction or award at the prime award level.</td><td>8510186794!BATTERY POWER SUPPLY</td></tr><tr><td>period_of_performance_start_date</td><td>Agreed start date for the contract's requirements.</td><td>2023-10-02</td></tr><tr><td>period_of_performance_current_end_date</td><td>Scheduled completion date for the contract.</td><td>2023-11-01</td></tr><tr><td>period_of_performance_potential_end_date</td><td>Date when awardee effort is completed if all potential options were exercised.</td><td>2023-11-01</td></tr><tr><td>extension_days_available</td><td>Number of days available for extension.</td><td>0.0</td></tr><tr><td>time_to_start_performance</td><td>Number of days between the action date and the period of performance start date.</td><td>0.0</td></tr><tr><td>modification_number</td><td>Identifier of an action indicating the specific change to the initial award.</td><td>0</td></tr><tr><td>last_modified_date</td><td>The date capturing the change or modification.</td><td>2023-10-02</td></tr><tr><td>recipient_name</td><td>The name of the awardee or recipient associated with the unique identifier.</td><td>TESLA INDUSTRIES, INC.</td></tr><tr><td>recipient_uei</td><td>Unique Entity Identifier of the recipient organization.</td><td>WK5RYJL58YY9</td></tr></tbody></table>

### Government Transactions

<table><thead><tr><th>Column Name</th><th width="265">Description</th><th>Example</th></tr></thead><tbody><tr><td>contract_transaction_unique_key</td><td>A system-generated key used to uniquely identify each contract transaction record. It's a concatenation of various elements like agencyID, PIID, etc., with '<em>none</em>' used for blank fields.</td><td>9700_9700_8Z03_0_DAAB1502D1002_0</td></tr><tr><td>federal_action_obligation</td><td>Amount of the Federal government’s obligation, de-obligation, or liability, in dollars, for a transaction.</td><td>248398.0</td></tr><tr><td>transaction_description</td><td>Description of the transaction or award.</td><td>CLIN 0129AA AST - MESSAGING TECHNOLOGIES</td></tr><tr><td>contract_award_unique_key</td><td>Unique key to identify the prime award. It's a concatenation of elements such as PIID, agencyID, ParentAwardId, and Referenced IDV Agency Identifier, with '<em>none</em>' for blank fields.</td><td>CONT_AWD_8Z03_9700_DAAB1502D1002_9700</td></tr><tr><td>last_modified_date</td><td>Date when the transaction record was last modified.</td><td>2019-10-16T00:00:00</td></tr></tbody></table>

###

### Product Specifications

| Column Name                               | Description                                                                                                                                               | Example                                                        |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| ticker                                    | Stock ticker symbol identifying the company.                                                                                                              | TSLA                                                           |
| contract\_award\_unique\_key              | Unique key to identify the prime award, consisting of concatenation of elements like PIID, agencyID, ParentAwardId, and Referenced IDV Agency Identifier. | CONT\_AWD\_SPE7LX20F345T\_9700\_SPE7LX18D0042\_9700            |
| product\_or\_service\_code\_description   | Description explaining the meaning of the product or service code.                                                                                        | CONVERTERS, ELECTRICAL, NONROTATING                            |
| naics\_code                               | North American Industrial Classification System Code assigned to the solicitation and resulting award.                                                    | 335999.0                                                       |
| naics\_description                        | The title associated with the NAICS Code.                                                                                                                 | ALL OTHER MISCELLANEOUS ELECTRICAL EQUIPMENT AND COMPONENT MFG |
| country\_of\_product\_or\_service\_origin | Country of origin of the product or service.                                                                                                              | UNITED STATES                                                  |
| place\_of\_manufacture                    | Description explaining the place of manufacture.                                                                                                          | MFG IN U.S.                                                    |
| epa\_designated\_product                  | Description explaining the EPA-Designated Product Field.                                                                                                  | NOT REQUIRED                                                   |
| recovered\_materials\_sustainability      | Description explaining the Recovered Materials/Sustainability Field.                                                                                      | NO CLAUSES INCLUDED AND NO SUSTAINABILITY INCLUDED             |

### Entity Specification

| Column Name             | Description                                                                                                                                | Example                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------- |
| ticker                  | Stock ticker symbol identifying the company.                                                                                               | TSLA                   |
| recipient\_uei          | Unique Entity Identifier (UEI) of the recipient organization, used in financial and business reporting processes.                          | WK5RYJL58YY9           |
| recipient\_parent\_uei  | Unique Entity Identifier (UEI) of the highest-level parent organization of the recipient.                                                  | WK5RYJL58YY9           |
| recipient\_name         | The name of the awardee or recipient that relates to the unique identifier, as filed in formation documents with individual states.        | TESLA INDUSTRIES, INC. |
| recipient\_parent\_name | The name of the ultimate parent of the awardee or recipient.                                                                               | TESLA INDUSTRIES, INC. |
| names                   | A name associated with the recipient entity, derived during data processing and matching.                                                  | TESLA INDUSTRIES, INC. |
| similarity              | A score representing the similarity between the 'names' field and a corresponding entity in another dataset, used for data matching.       | 0.9562                 |
| bloomberg\_share\_id    | Bloomberg Share ID, a unique identifier for a share class at the Bloomberg level, obtained through data matching with Bloomberg's dataset. | BBG001SQKGD7           |

For the misstatements, all of the variables have been changed into negative indicators, so that when the company overreports the financial health and corrects it later on, that is a negative sign.

### Location Dictionary

| Column Name                                    | Description                                                                                                                                            | Example                                    |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| ticker                                         | Stock ticker symbol identifying the company.                                                                                                           | TSLA                                       |
| contract\_award\_unique\_key                   | Unique key to identify the prime award, a concatenation of PIID, agencyID, ParentAwardId, and Referenced IDV Agency Identifier.                        | CONT\_AWD\_0542\_9700\_SPM7MX13D0089\_9700 |
| recipient\_country\_name                       | The name corresponding to the country code of the awardee or recipient.                                                                                | UNITED STATES                              |
| recipient\_address\_line\_1                    | First line of the awardee or recipient’s legal business address.                                                                                       | 109 CENTERPOINT BLVD                       |
| recipient\_city\_name                          | Name of the city in which the awardee or recipient’s legal business address is located.                                                                | NEW CASTLE                                 |
| recipient\_county\_name                        | Name of the county in which the awardee or recipient’s legal business address is located.                                                              | NEW CASTLE                                 |
| recipient\_state\_code                         | United States Postal Service two-letter abbreviation for the state or territory in which the awardee or recipient’s legal business address is located. | DE                                         |
| recipient\_state\_name                         | The name or abbreviation for the state, territory, or province in which the award recipient's legal business address is located.                       | DELAWARE                                   |
| recipient\_zip\_4\_code                        | USPS zoning code associated with the awardee or recipient’s legal business address for domestic recipients only.                                       | 197204180                                  |
| primary\_place\_of\_performance\_country\_code | Country code where the predominant performance of the award will be accomplished.                                                                      | USA                                        |
| primary\_place\_of\_performance\_country\_name | Name of the country where the predominant performance of the award will be accomplished.                                                               | UNITED STATES                              |
| primary\_place\_of\_performance\_city\_name    | The name of the city where the predominant performance of the award will be accomplished.                                                              | NEW CASTLE                                 |
| primary\_place\_of\_performance\_county\_name  | The name of the county where the predominant performance of the award will be accomplished.                                                            | NEW CASTLE                                 |
| primary\_place\_of\_performance\_state\_code   | USPS two-letter abbreviation for the state or territory indicating where the predominant performance of the award will be accomplished.                | DE                                         |
| primary\_place\_of\_performance\_state\_name   | The name of the state or territory where the predominant performance of the award will be accomplished.                                                | DELAWARE                                   |
| primary\_place\_of\_performance\_zip\_4        | ZIP code identifying where the predominant performance of the award will be accomplished.                                                              | 197204180                                  |
| same\_country                                  | Is the place of performance the same as the location of the recepient                                                                                  | 1                                          |
| same\_state                                    | Is the place of performance the same as the location of the recepient                                                                                  | 1                                          |

### Competition Dictionary

| Column Name                  | Description                                                                                                                     | Example                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| ticker                       | Stock ticker symbol identifying the company.                                                                                    | TSLA                                              |
| contract\_award\_unique\_key | Unique key to identify the prime award, a concatenation of PIID, agencyID, ParentAwardId, and Referenced IDV Agency Identifier. | CONT\_AWD\_0162\_9700\_SPM43003D4053\_9700        |
| extent\_competed             | Description explaining the meaning of the code provided in the Extent Competed Field.                                           | FULL AND OPEN COMPETITION AFTER EXCLUSION OF S... |
| number\_of\_offers\_received | The number of actual offers/bids received in response to the solicitation.                                                      | 2.0                                               |
| solicitation\_procedures     | Description explaining the meaning of the code provided in the Solicitation Procedures Field.                                   | ONLY ONE SOURCE                                   |

### Compensation

| Column Name                             | Description                                                                                                                                         | Example                        |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| ticker                                  | Stock ticker symbol identifying the company.                                                                                                        | ACCA                           |
| date                                    | Date of the record.                                                                                                                                 | 2018-10-31                     |
| recipient\_uei                          | Unique Entity Identifier (UEI) of the recipient organization, used in financial and business reporting processes.                                   | K5TBNBLVG1F8                   |
| recipient\_name                         | The name of the awardee or recipient that relates to the unique identifier, as filed in formation documents with individual states.                 | ID TECHNOLOGIES, LLC           |
| recipient\_parent\_name                 | The name of the ultimate parent of the awardee or recipient.                                                                                        | ACACIA INVESTMENT HOLDINGS LLC |
| highly\_compensated\_officer\_1\_name   | The name of an individual identified as one of the five most highly compensated "Executives."                                                       | CHRISTOPHER OLIVER             |
| highly\_compensated\_officer\_1\_amount | The cash and noncash dollar value earned by the first of the five most highly compensated “Executives” during the awardee's preceding fiscal year.  | 485518.12500                   |
| highly\_compensated\_officer\_2\_name   | The name of an individual identified as the second of the five most highly compensated "Executives."                                                | DYLAN CONNER                   |
| highly\_compensated\_officer\_2\_amount | The cash and noncash dollar value earned by the second of the five most highly compensated “Executives” during the awardee's preceding fiscal year. | 820596.2500                    |
| highly\_compensated\_officer\_3\_name   | The name of an individual identified as the third of the five most highly compensated "Executives."                                                 | GAVIN LONG                     |
| highly\_compensated\_officer\_3\_amount | The cash and noncash dollar value earned by the third of the five most highly compensated “Executives” during the awardee's preceding fiscal year.  | 519297.12500                   |
| highly\_compensated\_officer\_4\_name   | The name of an individual identified as the fourth of the five most highly compensated "Executives."                                                | JEFFERY PANEBIANCO             |
| highly\_compensated\_officer\_4\_amount | The cash and noncash dollar value earned by the fourth of the five most highly compensated “Executives” during the awardee's preceding fiscal year. | 818678.1250                    |
| highly\_compensated\_officer\_5\_name   | The name of an individual identified as the fifth of the five most highly compensated "Executives."                                                 | THOMAS BRADY                   |
| highly\_compensated\_officer\_5\_amount | The cash and noncash dollar value earned by the fifth of the five most highly compensated “Executives” during the awardee's preceding fiscal year.  | 365064.81250                   |

##

## Explanations

### Importance for Investors

Understanding these tables is essential for investors:

* **Risk Assessment**: By analyzing the Misstatement and its industry-adjusted tables, investors can gauge the risk associated with a company's financial reporting.
* **Comparative Analysis**: The industry-adjusted tables enable investors to compare companies within the same sector on a like-for-like basis, making the analysis more relevant and accurate.
* **Informed Decision-Making**: Comprehensive data covering raw financials and industry-adjusted scores empowers investors to make well-informed investment decisions.

***
