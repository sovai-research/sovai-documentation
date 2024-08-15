---
description: >-
  A ticker matched lobbying data to see fine-grained corporate lobbying
  behaviour.
---

# 🎙️ Lobbying Data

{% hint style="info" %}
Data is updated weekly as data arrives after market close US-EST time.
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Factor Signals Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/tutorials/Factor%20Model.ipynb)

<table data-column-title-hidden data-view="cards"><thead><tr><th>Category</th><th>Details</th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>Lobbying Filings</td></tr><tr><td><strong>Models Used</strong></td><td>Parsing, Scraping</td></tr><tr><td><strong>Model Outputs</strong></td><td>Lobbying Data</td></tr></tbody></table>

Diversified selection of ratios for factor development or bottum-up equity selection strategies.

***

## Lobbying Dataset&#x20;

This section covers the usage of the lobbying dataset. The dataset can be accessed using the sov.data function from our data library.

### Lobbying Dataset

The Lobbying dataset provides detailed information on lobbying activities, including client information, spending, and lobbying issues for various companies.

<pre class="language-python"><code class="lang-python"><strong>import sovai as sov
</strong><strong>df_lobbying = sov.data("lobbying/public")
</strong></code></pre>

### Accessing Specific Tickers

You can also retrieve data for specific tickers. For example:

```python
df_ticker_lobbying = sov.data("lobbying/public", tickers=["WFC", "EXPGY"])
```

This documentation provides a clear guide on how to access the dataset, and can be easily extended or modified as needed for additional details.

### Data Dictionary

| Column Name                       | Description                                                             |
| --------------------------------- | ----------------------------------------------------------------------- |
| client                            | Name of the client company                                              |
| client\_description               | Description of the client's business                                    |
| spend                             | Amount spent on lobbying                                                |
| transaction\_type                 | Type of transaction (e.g., lobbying\_income, direct\_lobbying\_expense) |
| filing\_type                      | Type of filing                                                          |
| lobby\_description                | Description of lobbying activities                                      |
| issue\_codes                      | Codes representing the issues lobbied on                                |
| government\_entity\_details       | Government entities involved                                            |
| quarter                           | Quarter of the lobbying activity                                        |
| effective\_date                   | Start date of the lobbying activity                                     |
| termination\_date                 | End date of the lobbying activity (if applicable)                       |
| client\_state                     | State of the client                                                     |
| client\_country                   | Country of the client                                                   |
| client\_id                        | Unique identifier for the client                                        |
| government\_lobby                 | Indicator for government lobbying                                       |
| performing\_own\_lobbying         | Indicator if the client is performing their own lobbying                |
| registrant\_dt\_updated           | Date the registrant information was updated                             |
| registrant\_name                  | Name of the lobbying registrant                                         |
| registrant\_address               | Address of the lobbying registrant                                      |
| registrant\_id                    | Unique identifier for the registrant                                    |
| registrant\_description           | Description of the registrant                                           |
| registrant\_contact\_name         | Contact name for the registrant                                         |
| registrant\_house\_registrant\_id | House ID for the registrant                                             |
| registrant\_contact\_telephone    | Contact telephone for the registrant                                    |
| lobbyist\_full\_names             | Names of the lobbyists involved                                         |
| lobbyist\_ids                     | Unique identifiers for the lobbyists                                    |
| previous\_goverment\_positions    | Previous government positions held by lobbyists                         |
| lobbyist\_new\_statuses           | New status indicators for lobbyists                                     |
| client\_url                       | URL for client information                                              |
| registrant\_url                   | URL for registrant information                                          |
| filing\_url                       | URL for the filing                                                      |
| filing\_id                        | Unique identifier for the filing                                        |
| unique\_id                        | Unique identifier for the record                                        |
| match                             | Matched client name                                                     |
| date\_time                        | Date and time of the record                                             |
| ticker                            | Stock ticker symbol of the client company                               |
| date                              | Date of the lobbying activity                                           |

### Potential Use Cases

1. Corporate Influence Analysis: Examine how companies allocate resources to influence policy-making.
2. Sector Trends: Identify trends in lobbying activities across different sectors or industries.
3. Regulatory Impact Assessment: Analyze the relationship between lobbying efforts and regulatory outcomes.
4. ESG Research: Incorporate lobbying data into Environmental, Social, and Governance (ESG) assessments.
5. Political Risk Analysis: Evaluate potential political risks for companies based on their lobbying activities.
6. Corporate Strategy Insights: Gain insights into companies' strategic priorities by analyzing their lobbying focus areas.
7. Competitive Intelligence: Compare lobbying activities among competitors in the same industry.
8. Public Policy Research: Study the influence of corporate lobbying on public policy development.
9. Investor Due Diligence: Provide additional context for investor research and due diligence processes.
10. Transparency Reporting: Support corporate transparency initiatives by analyzing and reporting on lobbying activities.&#x20;

This dataset forms a comprehensive resource for analyzing corporate lobbying activities, enabling detailed examination of spending patterns, issue focus, and potential policy influences across different companies and sectors.

***
