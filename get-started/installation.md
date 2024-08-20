---
description: Learn how to install Sovai
---

# 💻 Installation

{% hint style="info" %}
**Sovai is now available**. `pip install sovai` to try it. Check out this example [Notebook](https://colab.research.google.com/drive/1aM09QsbkjPOfG1SnF4Jv-tSaE4wuwdhS?usp=sharing).
{% endhint %}

Install Sovai with Python's pip package manager.

```shell
pip install sovai
```

## Install

Sovai is tested and supported on the following 64-bit systems:

* Python 3.6 – 3.11
* Python 3.9 for Ubuntu only
* Ubuntu 16.04 or later
* Windows 7 or later

## &#x20;Environment

In order to avoid potential conflicts with other packages, it is strongly recommended to use a virtual environment, e.g. python3 virtualenv (see [python3 virtualenv documentation](https://docs.python.org/3/tutorial/venv.html)).

```sh
# create a virtual environment
python -m venv yourenvname

# activate the virtual environment
source yourenvname/bin/activate  # For Unix/Linux
yourenvname\Scripts\activate  # For Windows

# install sovai
pip install sovai

# create notebook kernel
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

{% hint style="info" %}
**NOTE:** We are actively working on reducing default dependencies in the next major release. We intend to support functionality level and module-specific install in the future. For example: `pip install sovai[nlp].`
{% endhint %}

## Building from source

To install the package directly from GitHub (latest source), use the following command:

```bash
pip install git+https://github.com/sovai/sovai.git#egg=pycaret
```

Don't forget to include the `#egg=sovai` part to explicitly name the project, this way pip can track metadata for it without having to have run the `setup.py` script.

#### Run the tests:

To launch the test suite, run the following command from outside the source directory:

```bash
pytest sovai
```

## Docker

Docker uses containers to create virtual environments that isolate a Sovai installation from the rest of the system. Sovai docker comes pre-installed with a Notebook environment. that can share resources with its host machine (access directories, use the GPU, connect to the Internet, etc.). The Sovai Docker images are tested for each release.

```bash
docker run -p 8888:8888 sovai/slim
```

For docker image with full version:

```bash
docker run -p 8888:8888 sovai/full
```

To learn more, check out [this documentation](https://hub.docker.com/r/pycaret/full).
