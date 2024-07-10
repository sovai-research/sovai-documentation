---
description: >-
  This dataset contains information about movie producers, their movies, and the
  corresponding box office performance.
---

# 🎦 Box Office Stats

### Data Access

#### Retrieving Data

Fetch the latest index data using the SDK:

```python
from sovai import sov 
df_movies = sov.data("movies/boxoffice")
```

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

### Data Dictionary

| Column Name          | Data Type | Description                                                                | Example                                             |
| -------------------- | --------- | -------------------------------------------------------------------------- | --------------------------------------------------- |
| ticker               | string    | Ticker symbol of the movie producer company                                | "ZEEL"                                              |
| date                 | date      | Date of the movie's box office performance                                 | 2022-03-18                                          |
| title                | string    | Title of the movie                                                         | "The Kashmir Files"                                 |
| distributor          | string    | Distributor of the movie                                                   | "Zee Studios"                                       |
| gross                | integer   | Gross box office revenue for the movie on the specified date               | 413000                                              |
| percent\_yd          | float     | Percentage change in gross revenue compared to the previous day            | 0.0                                                 |
| percent\_lw          | float     | Percentage change in gross revenue compared to the previous week           | 0.2                                                 |
| theaters             | integer   | Number of theaters screening the movie on the specified date               | 230                                                 |
| per\_theater         | float     | Average gross revenue per theater on the specified date                    | 1796.0                                              |
| total\_gross         | integer   | Cumulative gross box office revenue for the movie up to the specified date | 413000                                              |
| days\_in\_release    | integer   | Number of days the movie has been in release as of the specified date      | 1                                                   |
| parent\_company      | string    | Parent company of the movie producer                                       | "Zee Entertainment Enterprises Limited"             |
| distributor\_address | string    | Address of the movie distributor                                           | "Laxmi Industrial Estate, Off New Link Road, An..." |
| distributor\_website | string    | Website of the movie distributor                                           | "https://www.zee.com/"                              |
| release\_date        | date      | Initial release date of the movie                                          | 2022-03-17                                          |

### Dataset Structure

The dataset is organized as a table with 228,484 rows and 15 columns. Each row represents a specific movie's box office performance on a particular date.

### Data Types

The dataset contains the following data types:

* String: ticker, title, distributor, parent\_company, distributor\_address, distributor\_website
* Date: date, release\_date
* Integer: gross, theaters, total\_gross, days\_in\_release
* Float: percent\_yd, percent\_lw, per\_theater

### Missing Values

If a movie does not have any data for a particular column on a specific date, the corresponding cell may contain missing values.

### Example Rows

Here are a few example rows from the dataset:

| ticker | date       | title             | distributor   | gross  | percent\_yd | percent\_lw | theaters | per\_theater | total\_gross | days\_in\_release | parent\_company                       | distributor\_address                              | distributor\_website        | release\_date |
| ------ | ---------- | ----------------- | ------------- | ------ | ----------- | ----------- | -------- | ------------ | ------------ | ----------------- | ------------------------------------- | ------------------------------------------------- | --------------------------- | ------------- |
| 600579 | 2011-02-11 | Raymond Did It    | Plastic Age … | 2999   | 0.0         | 0.0         | 1.0      | 2999.0       | 2999         | 1                 | KraussMaffei Group                    | 7295 Tellier St, Montreal, Quebec H1N 3S9, CA     | https://plastic-age.com/en/ | 2011-02-10    |
| 600579 | 2011-02-12 | Raymond Did It    | Plastic Age … | 193    | -0.94       | 0.0         | 1.0      | 193.0        | 3192         | 2                 | KraussMaffei Group                    | 7295 Tellier St, Montreal, Quebec H1N 3S9, CA     | https://plastic-age.com/en/ | 2011-02-10    |
| ZEEL   | 2022-03-18 | The Kashmir Files | Zee Studios   | 413000 | 0.0         | 0.0         | 230.0    | 1796.0       | 413000       | 1                 | Zee Entertainment Enterprises Limited | Laxmi Industrial Estate, Off New Link Road, An... | https://www.zee.com/        | 2022-03-17    |

This data dictionary provides an overview of the movie producer and movie dataset, including the column descriptions, data types, examples, and sample rows.
