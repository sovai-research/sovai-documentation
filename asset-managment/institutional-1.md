---
description: >-
  This module provides a comprehensive set of tools for portfolio managers and
  quantitative analysts to optimize asset allocation strategies and evaluate
  their performance.
---

# 🗣️ Weight Optimization

### Key Features

* Multiple optimization strategies
* Comprehensive performance analysis
* Risk-adjusted return metrics
* Portfolio composition visualization
* Drawdown and contribution analysis
* Correlation and clustering analysis
* Daily weight tracking

### Usage

To use the Weight Optimization module, you first need to prepare your dataset. Here's an example of how to set up and run the optimization:

```python
import sovai as sov

# Authenticate
sov.token_auth(token="your_authentication_token")

# Prepare your data
df_price = sov.data("market/closeadj")
df_mega = df_price.select_stocks("mega").date_range("2000-01-01")
df_returns = df_mega.calculate_returns().dropna(axis=1, how="any")

# Select the most uncorrelated stocks
feature_importance = df_returns.importance()
df_select = df_returns[feature_importance["feature"].head(25)]

# Run weight optimization
portfolio = df_select.weight_optimization()
```

## Overall Portfolio Analysis

### **Sharpe Ratio Distribution**

Shows the distribution of Sharpe ratios across different strategies, helping to understand the consistency of risk-adjusted returns.

```python
portfolio.sharpe_plot
```

<figure><img src="../.gitbook/assets/image (11).png" alt=""><figcaption></figcaption></figure>

### **Cumulative Returns Plot**

Displays the cumulative returns of all portfolio strategies over time, allowing for easy comparison of overall performance.

```python
portfolio.return_plot
```

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>

### **Overall Composition Plot**

Illustrates the asset allocation of all strategies, allowing for a comparison of how different models allocate capital.

```python
portfolio.composition_plot
```

<figure><img src="../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

### **Best Performing Model**

Identifies the strategy that performed best according to the Sharpe ratio.

```python
portfolio.best_model
```

```
'NCO'
```

### **Performance Summary**

Provides a comprehensive summary of key performance metrics for all strategies, including returns, volatility, Sharpe ratio, and more.

```python
portfolio.performance_report
```

<figure><img src="../.gitbook/assets/image (14).png" alt=""><figcaption></figcaption></figure>

## Model-Specific Analysis

For model-specific analysis, replace "model\_name" with the actual model name (e.g., HRP, HERC, NCO, or EQUAL).

### **Cumulative Returns**

```python
portfolio["model_name"].backtest_plot
```

<figure><img src="../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>

Displays the cumulative returns of the specific model over the backtesting period.

### **Backtest Report**

Detailed performance statistics from the backtesting period for the specific model.

```python
portfolio["model_name"].backtest_report
```

<figure><img src="../.gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

### **Rolling Sharpe Ratio**

Visualizes how the Sharpe ratio of the model changes over time, indicating consistency of performance.

```python
portfolio["model_name"].sharpe_rolling_plot
```

<figure><img src="../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

### **Model Composition**

Illustrates the asset allocation for the specific model.

```python
portfolio["model_name"].composition_plot
```

<figure><img src="../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

### **Drawdown Contribution**

Shows which assets contribute most to the portfolio's drawdowns, helping identify risk sources.

```python
portfolio["model_name"].drawdown_contribution_plot
```

<figure><img src="../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

### **Sharpe Ratio Contribution**

Indicates which assets contribute most to the portfolio's Sharpe ratio, highlighting return drivers.

```python
portfolio["model_name"].sharpe_contribution_plot
```

<figure><img src="../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

### **Correlation Heatmap**

Displays the correlation structure of assets used in the model (not available for EQUAL).

```python
portfolio["model_name"].heatmap_plot
```

<figure><img src="../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### **Clustering Dendrogram**

Visualizes the hierarchical clustering of assets used in the model (not available for EQUAL).

```python
portfolio["model_name"].cluster_plot
```

<figure><img src="../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

### **Current Recommended Allocation**

Provides the model's most recent recommended asset allocation.

```python
portfolio["model_name"].recommended_allocation
```

<figure><img src="../.gitbook/assets/image (23).png" alt=""><figcaption></figcaption></figure>

### **Sharpe Ratio Distribution**

Shows the distribution of Sharpe ratio helping to understand the consistency of risk-adjusted returns.

```python
portfolio["model_name"].recommended_allocation
```

<figure><img src="../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

### **Daily Weights**

Shows how the model's asset allocation changes day-by-day over the backtesting period.

```python
portfolio["model_name"].daily_weights
```

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>
