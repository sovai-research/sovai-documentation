# 🚀 Quick Start

**Only works for paying subscribers, purchase your API key** [<mark style="color:purple;">**`here`**</mark>](https://sov.ai/subscribe)**.**&#x20;

<pre class="language-python"><code class="lang-python"><strong>import sovai as sov
</strong><strong>sov.token_auth(token="add_your_subscriber_token_here")
</strong></code></pre>

## Installation

To use Sovai's python module you can install `sovai`.

```
pip install sovai[full]
```

{% hint style="success" %}
**The best way to familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](tutorials.md)
{% endhint %}

### Data

If you only want to download data into pandas please use the much lighter package.&#x20;

```
pip install sovai
```

```python
import sovai as sov
sov.data("query")
```

## Commands

Utilize various commands to interact with datasets:, [`data`](quickstart.md#download-datasets) ,[`plots`](quickstart.md#visualizing-data), and [`reports`](quickstart.md#running-reports)`.`

* `sov.data('query')`: Retrieve data based on the specified query.
* `sov.plots('query')`: Generate plots for visual analysis.
* `sov.reports('query')`: Access reports summarizing predictions.

## Authenticate Account: <mark style="color:blue;">`token_auth()`</mark>

There are two ways to authenticate your requests. Get your token [here](https://sov.ai/home).

<pre class="language-python"><code class="lang-python">import sovai as sov

# 1. Method 1: Configuration API connection
<strong>sov.token_auth(token="add_your_token_here")
</strong>
# 2. Method 2: Or read token from .env file e.g API_TOKEN=super_secret_token
sov.read_key('.env')
</code></pre>

## Download Data: : <mark style="color:blue;">`data()`</mark>

Once authenticated, downloading datasets becomes easy.

```python
# Example data retrieval
gs_df = sov.data("bankruptcy/monthly")
```

## Visualize Data: <mark style="color:blue;">`plot()`</mark>

#### Unique Plots

Certain datasets have unique visualizations that you access from their respective pages.

```python
# Calls the 'bankruptcy' dataset and the associated chart_type
sov.plot('bankruptcy', chart_type='compare')
```

#### Universal Plots

Other datasets can use panda's built-in plots.

```python
df_risks = sov.data("risks")
df_risks[["MARKET_RISK","TURING_RISK"]].tail(15400).plot()
```

## Running Reports: <mark style="color:blue;">`report()`</mark>

Run report to explore the dataset.

```python
sov.report("corprisk/accounting",report_type="sector-top")
```

We can also make use of pandas' built-in functions to run queries on top of the data.

```python
df_risks.query("ticker == 'CGRNQ'")
```

