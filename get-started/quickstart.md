---
description: Quick start guide to Sovai
---

# 🚀 Quickstart

{% code fullWidth="false" %}
```bash
!pip install sovai
```
{% endcode %}

Please note that this only works for [<mark style="color:purple;">`paying subscribers`</mark>](https://sov.ai/home)!&#x20;

### [`Got to Tutorials` ](tutorials.md)

{% hint style="info" %}
**To familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](tutorials.md)&#x20;
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

## Authenticate Account:  <mark style="color:blue;">sov.token\_auth()</mark>

You will be unable to access **Sovai Datasets** without authenticating your requests.&#x20;

There are two ways to authenticate your requests. Get your token [here](https://sov.ai/home).&#x20;

<pre class="language-python"><code class="lang-python">import sovai as sov

# 1. Method 1: Configuration API connection
<strong>sov.token_auth(token="add_your_token_here")
</strong>
# 2. Method 2: Or read token from .env file e.g API_TOKEN=super_secret_token
sov.read_key('.env')
</code></pre>



## Download Data: :  <mark style="color:blue;">sov.data()</mark>

Once this is done, downloading datasets becomes as easy as using this.

```python
# Retrieve data
gs_df = sov.data("bankruptcy/monthly")
```

We access  tables "<mark style="color:blue;">corprisk</mark>", "<mark style="color:blue;">breakout</mark>", "<mark style="color:blue;">news"</mark>, "<mark style="color:blue;">institutional</mark>", "<mark style="color:blue;">wikipedia</mark>", and many more from the **data repository**.&#x20;



## Visualize Data: <mark style="color:blue;">sov.plot()</mark>

#### Unique Plots

Certain datasets have unique visualization that you access from their respective pages.&#x20;

```python
sov.plot('bankruptcy', chart_type='compare')
```

In these scenarios, you would directly call up the dataset, in this case **'bankruptcy'** and the associated **chart\_type.**&#x20;

#### Universal Plots

Some visualizations are universally applicable to multiple datasets. We could also rely heavily on the built-in plots in pandas.&#x20;

```python
df_risks = sov.data("risks")
df_risks[["MARKET_RISK","TURING_RISK"]].tail(15400).plot()
```



## Running Reports: <mark style="color:blue;">sov.report()</mark>

Another option is for us to run reports on the dataset, which largely allows us to explore the dataset.&#x20;

```python
sov.report("corprisk/accounting",report_type="sector-top")
```

We can also make use of pandas' built in functions to run queries on top of the data.&#x20;

```python
df_risks.query("ticker == 'CGRNQ'")
```



## Running Computation: <mark style="color:blue;">sov.compute()</mark>

Sovai simplifies many calculations that would otherwise take many lines to compute. We also write the code to be as fast as possible .

Here is an example of one line of code needed to calculate Principal Components.&#x20;

```python
pca_df = sov.compute("pca",df_risks)
```

This is an example of calculating a distance-matrix on a dataset.

```python
df_distance = sov.compute('distance-matrix', on="ticker", df=df_risks)
```



## Custom Studies: <mark style="color:blue;">sov.custom()</mark>

<mark style="background-color:red;">Still a work in progress.</mark>

Studies include more advanced methods than calculations, and currently include software for portfolio-optimization, and time-series forecasts.&#x20;

### Forecasting

```python
df_future = sov.forecast(df_risks, horizon=12)
```

### Portfolio Optimization

```
df_future = sov.optimize(df_positions, scale="week")
```

Our studies is a growing area of research and we will keep expanding and enchancing our offering in this space.&#x20;
