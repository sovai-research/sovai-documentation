# 💻 Installation

## Install

<pre class="language-python"><code class="lang-python"><strong>import sovai as sov
</strong><strong>sov.token_auth(token="add_your_subscriber_token_here")
</strong></code></pre>

### Full package

<pre><code><strong>pip install sovai[full]
</strong></code></pre>

{% hint style="success" %}
**The best way to familiarize yourself with this powerful library is to head straight to the**[ **tutorial section.**](tutorials.md)
{% endhint %}

### Data package

If you only want to download data into pandas please use the much lighter package.&#x20;

```
pip install sovai
```

```python
import sovai as sov
sov.data("query")
```

## Environment

Sovai is tested and supported on the following 64-bit systems:

* Python 3.6 – 3.11
* Python 3.9 for Ubuntu only
* Ubuntu 16.04 or later
* Windows 7 or later

In order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment, e.g. [python3 virtualenv](https://docs.python.org/3/tutorial/venv.html).

```sh
# Create a virtual environment
python -m venv yourenvname

# Activate the virtual environment
source yourenvname/bin/activate  # For Unix/Linux
yourenvname\Scripts\activate  # For Windows

# Install sovai
pip install sovai

# Create notebook kernel
python -m ipykernel install --user --name yourenvname --display-name "display-name"
```

## Dependencies

Default dependencies that are installed with `pip install sovai` are [listed here](https://github.com/sovai-research/SovAI/blob/master/pyproject.toml).

#### Select the tab

{% tabs %}
{% tab title="requirements" %}
numpy>=1.20

scipy>=1.0&#x20;

pandas>=1.0

python-dateutil>=2.8

python-dotenv>=0.10

&#x20;requests>=2.20

&#x20;joblib>=1.0&#x20;

pyarrow>=5.0

&#x20;matplotlib>=3.0

&#x20;plotly>=5.0

&#x20;scikit-learn>=1.0

&#x20;numba>=0.50

&#x20;boto3>=1.20

&#x20;dash>=2.0

great-tables>=0.9

&#x20;polars>=0.20.30

&#x20;ruptures>=1.0

&#x20;shap>=0.40

&#x20;skfolio>=0.3

&#x20;statsforecast>=1.0

&#x20;tensorly>=0.6

&#x20;openai>=1.0

&#x20;mfles>=0.2

&#x20;pexpect>=4.9.0

&#x20;lightgbm>=4.5.0&#x20;

ipywidgets>=8.1.3

&#x20;polars-talib==0.1.3

&#x20;dash-bootstrap-components>=1.6.0
{% endtab %}

{% tab title="requirements-dev" %}
poetry>=1.0&#x20;

pytest>=6.0&#x20;

flake8>=3.9&#x20;

black>=21.0&#x20;

isort>=5.0&#x20;

mypy>=0.900
{% endtab %}
{% endtabs %}

## Docker

Docker uses containers to create virtual environments that isolate a Sovai installation from the rest of the system. Sovai docker comes pre-installed with a Notebook environment that can share resources with its host machine (access directories, use the GPU, connect to the Internet, etc.). The Sovai Docker images are tested for each release.

```bash
docker run -p 8888:8888 sovai/slim
```

For docker image with full version:

```bash
docker run -p 8888:8888 sovai/full
```
