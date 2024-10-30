---
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

# Statistical Investment Screening

**Only works for paying subscribers, purchase your API key** [<mark style="color:purple;">**`here`**</mark>](https://sov.ai/subscribe)**.**&#x20;

<pre class="language-python"><code class="lang-python">import sovai as sov
<strong>sov.token_auth(token="add_your_subscriber_token_here")
</strong></code></pre>

## Installation

To use Sovai's python module you can install `sovai`.

```
pip install sovai[full]
```

{% hint style="success" %}
**The best way to familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](get-started/tutorials.md)
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

### Provided Datasets

1. [Equity Datasets](realtime-datasets/equity-datasets/) - Data on publicly traded companies.
2. [Economic Datasets](realtime-datasets/equity-datasets/) - Data for economic forecasting.
3. [Sectorial Datasets](realtime-datasets/sectorial-datasets/) - Sector-specific data for predictive insights.

### Get Help

* The fastest way to get help is to email us at [d.snow@sov.ai](mailto:d.snow@sov.ai) for support.
* We also have a pretty active [Linkedin](https://www.linkedin.com/company/sovai/) page.

## Support us

:tada: For future use, star our [GitHub](https://github.com/sovai-research/sovai-public) repository (click the star button on the top right corner)
