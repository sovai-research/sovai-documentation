---
description: >-
  Sovai: A low-code machine learning and data library for investment managers
  using Python.
cover: >-
  https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?crop=entropy&cs=tinysrgb&fm=jpg&ixid=MnwxOTcwMjR8MHwxfHNlYXJjaHw1fHxncmFkaWVudHxlbnwwfHx8fDE2NzY4NTQ4Mjk&ixlib=rb-4.0.3&q=80
coverY: 0
layout:
  cover:
    visible: true
    size: full
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Python for Asset Management

**Only works if you purchase an API key i.e, only for** [<mark style="color:purple;">**`paying subscribers`**</mark>](https://sov.ai/)

<pre class="language-python"><code class="lang-python">import sovai as sov
<strong>sov.token_auth(token="add_your_subscriber_token_here")
</strong></code></pre>

## Installation

To use Sovai's python module you can install `SovAI`.

```
pip install sovai[full]
```

{% hint style="success" %}
**The best way to familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](get-started/tutorials.md)
{% endhint %}

### Data

If you only want to download data into pandas, i.e., run`sov.data()` then please use the much lighter package.&#x20;

```
pip install sovai
```

### Provided Datasets

1. [Equity Datasets](realtime-datasets/equity-datasets/) - Data on publicly traded companies.
2. [Economic Datasets](realtime-datasets/equity-datasets/) - Data for economic forecasting tasks.
3. [Sectorial Datasets](realtime-datasets/sectorial-datasets/) - Diverse sectors for predictive analysis.

### Forthcoming Datasets

Depending on the feedback we receive from users we can add the following datasets.

<table><thead><tr><th width="183">Prediction Data</th><th width="210">Core Datasets</th><th width="213">Sectorial Data</th><th>Premium Data</th></tr></thead><tbody><tr><td>Earnings Surprise</td><td>Congressional Trading</td><td>Box Office Data</td><td>Shipping Data</td></tr><tr><td>ETF Flows</td><td>Senatorial Trading</td><td>Walmart Products</td><td>Real Estate</td></tr><tr><td>Undervaluation</td><td>Patent Applications</td><td>Amazon Products</td><td>Entity Data</td></tr></tbody></table>

## Contribution

If you want to contribute to the project please reach out

{% hint style="info" %}
**Contribute!** If you would like to contribute to this project please get in touch [here](https://github.com/sovai-research/sovai-public/issues).
{% endhint %}

## Get Help

* The fastest way to get help is to email us at [d.snow@sov.ai](mailto:d.snow@sov.ai) for support.
* We also have a pretty active [Linkedin](https://www.linkedin.com/company/sovai/) page.

## Support us

#### _The most user-friendly machine learning library for quantamental investment managers._

:tada: For future use, star our [GitHub](https://github.com/sovai-research/sovai-public) repository (click the star button on the top right corner)
