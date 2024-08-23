---
icon: seal-exclamation
description: >-
  Chapter 7 and Chapter 11 bankruptcy predictions made easy for over 13,000 US
  publicly traded stocks.
---

# Bankruptcy Predictions

{% hint style="info" %}
Monthly corporate bankruptcy predictions arrive the **2nd of every month**_._
{% endhint %}

`Tutorials` are the best documentation — [<mark style="color:blue;">`Corporate Bankruptcy Tutorial`</mark>](https://colab.research.google.com/github/sovai-research/sovai-public/blob/main/notebooks/datasets/Bankruptcy%20Prediction.ipynb)

<table data-view="cards" data-full-width="false"><thead><tr><th></th><th></th></tr></thead><tbody><tr><td><strong>Input Datasets</strong></td><td>SEC Bankruptcies, Delistings, Market Data, Financial Statements</td></tr><tr><td><strong>Models Used</strong></td><td>CNN, LightGBM, RocketModel, AutoEncoder</td></tr><tr><td><strong>Model Outputs</strong></td><td>Calibrated Probabilities, Shapley Values</td></tr></tbody></table>

## Description

The model predicts the likelihood of bankruptcies in the next 6-months for US publicly listed companies using advanced machine learning models.

With an accuracy of around 89% and ROC-AUC of 85%, these models represent a large improvement over traditional methods of bankruptcy prediction for equity selection.



## Data Access

### **Monthly Probabilities**

**Specific Tickers**

```python
import sovai as sov
df_bankrupt = sov.data('bankruptcy', tickers=["MSFT","TSLA","META"])
```

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Specific Dates**

```python
import sovai as sov
df_bankrupt = sov.data('bankruptcy', start_date="2017-01-03", tickers=["MSFT"])
```

**All Data**

```python
import sovai as sov
df_bankrupt = sov.data('bankruptcy')
```

### Daily Probabilities

```python
import sovai as sov
df_bankrupt = sov.data('bankruptcy/daily', tickers=["MSFT","TSLA","META"])
```

The daily probabilities are experimental, and have a very short history of just a couple of months.

### Feature Importance (Shapleys)

```python
import sovai as sov
df_importance = sov.data('bankruptcy/shapleys', tickers=["MSFT","TSLA","META"])
```

Feature Importance (Shapley Values) calculates the contribution of each input variable (features) such as Debt, Assets, and Revenue to predict bankruptcy risk.

<figure><img src="../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>



## Data Dictionary

<table><thead><tr><th width="293">Name</th><th width="246">Description</th><th width="89">Type</th><th>Example</th></tr></thead><tbody><tr><td><code>ticker</code></td><td>Stock ticker symbol.</td><td>TEXT</td><td>"TSLA"</td></tr><tr><td><code>date</code></td><td>Record date.</td><td>DATE</td><td>2023-09-30</td></tr><tr><td><code>probability_light</code></td><td>LightGBM Boosting Model prediction.</td><td>FLOAT</td><td>1.46636</td></tr><tr><td><code>probability_convolution</code></td><td>CNN Model prediction for bankruptcies</td><td>FLOAT</td><td>0.135975</td></tr><tr><td><code>probability_rocket</code></td><td>Rocket Model prediction for time series classification</td><td>FLOAT</td><td>0.02514</td></tr><tr><td><code>probability_encoder</code></td><td>LightGBM and CNN autoencoders Model prediction.</td><td>FLOAT</td><td>0.587817</td></tr><tr><td><code>probability_fundamental</code></td><td>Prediction using accounting data only.</td><td>FLOAT</td><td>1.26148</td></tr><tr><td><code>probability</code></td><td>Average probability across models.</td><td>FLOAT</td><td>0.553823</td></tr><tr><td><code>sans_market</code></td><td>Fundamental prediction adjusted for market predictions.</td><td>FLOAT</td><td>-0.20488</td></tr><tr><td><code>volatility</code></td><td>Variability of model predictions.</td><td>FLOAT</td><td>0.62934</td></tr><tr><td><code>multiplier</code></td><td>Coefficient for model prediction calibration.</td><td>FLOAT</td><td>1.951868</td></tr><tr><td><code>version</code></td><td>Model/data record version.</td><td>INT</td><td>20240201</td></tr></tbody></table>

{% hint style="info" %}
When `sans_market` is <mark style="color:green;">positive</mark>, it means that the fundamentals show a larger predicted bankruptcy than what the market predicts **(stock might go down in medium term)** , when `sans_market` is <mark style="color:red;">negative</mark>, the market might have overreacted, and predict a larger probability of bankruptcy than what the fundamentals suggest **(stock might go up in medium term)**.
{% endhint %}

## Reports

### Sorting and Filtering

```python
import sovai as sov
sov.report("bankruptcy", report_type="ranking")
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Filter the outputs based on the top by **Sector**, **Marketcap**, and **Revenue** and bankruptcy risk. You can also change <mark style="color:blue;">`ranking`</mark> to <mark style="color:blue;">`change`</mark> to investigate the month on month change.

```python
sov.report("bankruptcy", report_type="sector-change")
```

## Plots

### Bankruptcy Comparison

```python
import sovai as sov
sov.plot('bankruptcy', chart_type='compare')
```

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Compare bankruptcy probabilities across different tickers.</p></figcaption></figure>

### Timed Feature Importance

```python
import sovai as sov
df = sov.plot("bankruptcy", chart_type="shapley", tickers=["TSLA"])
```

<figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>Examine how feature importance values evolve over time.</p></figcaption></figure>

### Total Feature Importance

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="stack", tickers=["DDD"])
```

<figure><img src="../../.gitbook/assets/image (6) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Bankruptcy and Returns

```python
import sovai as sov
df= sov.plot("bankruptcy", chart_type="line", tickers=["DDD"])
```

<figure><img src="../../.gitbook/assets/image (7) (1) (1) (1).png" alt=""><figcaption><p>Analyze the relationship between bankruptcy probabilities and stock prices.</p></figcaption></figure>

### **PCA Statistical Similarity**

```python
import sovai as sov
df= sov.plot("bankruptcy", chart_type="line", tickers=["DDD"])
```

<figure><img src="../../.gitbook/assets/image (8) (1) (1).png" alt=""><figcaption><p>Explore the principal component analysis to identify similar tickers.</p></figcaption></figure>

### Correlation Similarity

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="similar", tickers=["DDD"])
```

<figure><img src="../../.gitbook/assets/image (9) (1) (1).png" alt=""><figcaption><p>Discover correlated stocks based on bankruptcy risk profiles.</p></figcaption></figure>

### Trend Similarity

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="facet", tickers=["DDD"])
```

<figure><img src="../../.gitbook/assets/image (10) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Global Performance

### **Confusion Matrix**

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="confusion_global")
```

<figure><img src="../../.gitbook/assets/image (12) (1) (1).png" alt=""><figcaption></figcaption></figure>

### **Threshold Plots**

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="classification_global")
```

<figure><img src="../../.gitbook/assets/image (14) (1).png" alt=""><figcaption></figcaption></figure>

### **Lift Curve**

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="lift_global")
```

<figure><img src="../../.gitbook/assets/image (15) (1).png" alt=""><figcaption></figcaption></figure>

### Global Explainability

```python
import sovai as sov
sov.plot("bankruptcy", chart_type="time_global")
```

<figure><img src="../../.gitbook/assets/image (11) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Computations

Leverage advanced computational tools for deeper analysis:

*   **Distance Matrix:**

    ```python
    sov.compute('distance-matrix', on="attribute", df=dataframe)
    ```

    Assess the similarity between entities based on selected attributes.
*   **Percentile Calculation:**

    ```python
    sov.compute('percentile', on="attribute", df=dataframe)
    ```

    Calculate the relative standing of values within a dataset.
*   **Feature Mapping:**

    ```python
    sov.compute('map-accounting-features', df=dataframe)
    ```

    Map accounting features to standardized metrics.
*   **PCA Calculation:**

    ```python
    sov.compute('pca', df=dataframe)
    ```

    Perform principal component analysis for dimensionality reduction.

**For more advanced applications, see the tutotrial.**

***

## **Description**

The model attempts to predict the likelihood of bankruptcies in the next 6-months. The likelihood that companies would go bankrupt in the next 6-months is very low. The change of this value over time can also be very revealing. See for example: `sov.report("bankruptcy", report_type="sector-change")`

### **Advanced Modeling Techniques**:

* **The Boosting Model**: Utilizes LightGBM technology, integrating both fundamental and market data for accurate predictions.
* **The Convolutional Model**: Employs a Convolutional Neural Network (CNN) for efficient pattern recognition in market trends.
* **The Rocket Model**: Specializes in time series data, using random convolutional kernels for effective classification and forecasting.
* **The Encoder Model**: Combines LightGBM with CNN autoencoders, enhancing feature engineering for more precise predictions.
* **The Fundamental Model**: Focuses solely on fundamental data via LightGBM, without extra architectural layers, for straightforward financial analysis.

### Potential Use-cases

1. **Bankruptcy Prediction Analysis**: Offer insights into predicted corporate bankruptcies and identify key factors, clarifying main drivers across different cycles.
2. **Variable Impact Breakdown**: Analyze how each individual variable affects bankruptcy predictions, providing in-depth feature contribution insights.
3. **Temporal Feature Distribution Analysis**: Reveal how variables contribute to predictions over time, emphasizing key features in forecasting models.
4. **Correlation Discovery**: Identify stocks with similar bankruptcy probability trends, revealing correlated market behaviors.
5. **Probability Shift Overview**: Showcase changes in bankruptcy probabilities among correlated stocks, providing a comprehensive market perspective.
6. **Sentiment Inversion Analysis**: Convert bankruptcy predictions into positive sentiment indicators to gauge potential impacts on stock returns.
7. **Behavioral Similarity Mapping**: Locate stocks with similar behaviors to a selected reference, based on bankruptcy trends and PCA feature analysis.
