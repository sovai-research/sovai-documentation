---
description: Quick start guide to Sovai
---

# 🚀 Quickstart

{% code fullWidth="false" %}
```bash
!pip install sovai
```
{% endcode %}

Please note that this only works for [<mark style="color:purple;">`paying subscribers`</mark>](https://sov.ai/home)!

### [<mark style="color:orange;">`Go to Tutorials`</mark>](tutorials.md)

{% hint style="info" %}
**To familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](tutorials.md)
{% endhint %}

## Introduction

* [Download Datasets](quickstart.md#download-datasets)
* [Visualizing Data](quickstart.md#visualizing-data)
* [Running Reports](quickstart.md#running-reports)
* [Running Calculations](quickstart.md#running-calculations)
* [Performing Studies](quickstart.md#performing-studies)

### Commands

Utilize various commands to interact with datasets:, [`data`](quickstart.md#download-datasets) ,[`plot`](quickstart.md#visualizing-data), [`report`](quickstart.md#running-reports), and [`compute`](quickstart.md#running-calculations).

* `sov.data('query')`: Retrieve data based on the specified query.
* `sov.plots('query')`: Generate plots for visual analysis.
* `sov.reports('query')`: Access reports summarizing predictions.
* `sov.compute('query')`: Perform computations on the dataset.

## Example

## Authenticate Account: <mark style="color:blue;">sov.token\_auth()</mark>

You will be unable to access **Sovai Datasets** without authenticating your requests.

There are two ways to authenticate your requests. Get your token [here](https://sov.ai/home).

<pre class="language-python"><code class="lang-python">import sovai as sov

# 1. Method 1: Configuration API connection
<strong>sov.token_auth(token="add_your_token_here")
</strong>
# 2. Method 2: Or read token from .env file e.g API_TOKEN=super_secret_token
sov.read_key('.env')
</code></pre>

## Download Data: : <mark style="color:blue;">sov.data()</mark>

Once this is done, downloading datasets becomes as easy as using this.

```python
# Retrieve data
gs_df = sov.data("bankruptcy/monthly")
```

We access tables "<mark style="color:blue;">corprisk</mark>", "<mark style="color:blue;">breakout</mark>", "<mark style="color:blue;">news"</mark>, "<mark style="color:blue;">institutional</mark>", "<mark style="color:blue;">wikipedia</mark>", and many more from the **data repository**.

## Visualize Data: <mark style="color:blue;">sov.plot()</mark>

#### Unique Plots

Certain datasets have unique visualization that you access from their respective pages.

```python
sov.plot('bankruptcy', chart_type='compare')
```

In these scenarios, you would directly call up the dataset, in this case **'bankruptcy'** and the associated **chart\_type.**

#### Universal Plots

Some visualizations are universally applicable to multiple datasets. We could also rely heavily on the built-in plots in pandas.

```python
df_risks = sov.data("risks")
df_risks[["MARKET_RISK","TURING_RISK"]].tail(15400).plot()
```

## Running Reports: <mark style="color:blue;">sov.report()</mark>

Another option is for us to run reports on the dataset, which largely allows us to explore the dataset.

```python
sov.report("corprisk/accounting",report_type="sector-top")
```

We can also make use of pandas' built in functions to run queries on top of the data.

```python
df_risks.query("ticker == 'CGRNQ'")
```

