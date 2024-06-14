---
description: Learn how to install Sovai
---

# 💻 Installation

{% hint style="info" %}
**Sovai is now available**. `pip install sovai` to try it. Check out this example [Notebook](https://colab.research.google.com/drive/1\_H0sHYhzKGZDmgzrQLosuZAR3nOaL6CN?usp=sharing).
{% endhint %}

## Install

Sovai is tested and supported on the following 64-bit systems:

* Python 3.6 – 3.11
* Python 3.9 for Ubuntu only
* Ubuntu 16.04 or later
* Windows 7 or later

Install Sovai with Python's pip package manager.

```shell
pip install sovai
```

To install the full version (see dependencies below):

```bash
pip install sovai[full]
```

## Environment

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

{% hint style="warning" %}
Sovai is **not** yet compatible with sklearn>=0.23.2.
{% endhint %}

## Dependencies

* Default dependencies that are installed with `pip install sovai` are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements.txt).
* Optional dependencies that are installed with `sovai[full]` are [listed here](installation.md#install-from-pip).
* Testing requirements are [listed here](https://github.com/pycaret/pycaret/blob/master/requirements-test.txt).

#### Select the tab

{% tabs %}
{% tab title="requirements" %}
pandas

scipy<=1.5.4

seaborn

polars

matplotlib
{% endtab %}

{% tab title="requirements-optional" %}
shap

interpret<=0.2.4

tune-sklearn>=0.2.1

ray\[tune]>=1.0.0

hyperopt

optuna>=2.2.0

scikit-optimize>=0.8.1

psutil

catboost>=0.23.2

xgboost>=1.1.0

explainerdashboard

m2cgen

evidently

autoviz

fairlearn

fastapi

uvicorn

gradio

fugue>=0.6.5

boto3

azure-storage-blob

google-cloud-storage
{% endtab %}

{% tab title="requirements-test" %}
pytest

moto

codecov
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
