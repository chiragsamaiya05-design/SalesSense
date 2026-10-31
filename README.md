# SalesSense — Sales Analytics & Predictive Intelligence

<p align="center">
  <strong>Explore sales performance. Understand customers. Experiment with forecasting.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/ML-Scikit--learn-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Testing-Pytest-blue?logo=pytest" />
</p>

## Overview

SalesSense is an interactive sales analytics application developed using Python.

It helps analyze sales transactions, monitor revenue performance, understand customer purchasing behaviour and experiment with Machine Learning-based sales forecasting.

## Features

* Interactive sales analytics dashboard.
* Revenue and order monitoring.
* Product and category performance analysis.
* Regional sales analysis.
* Customer segmentation using K-Means.
* Automated business insights.
* Experimental sales forecasting using Random Forest.
* Interactive data visualization.
* CSV report export.
* Data preprocessing and validation.

## Dashboard Modules

| Module                | Description                                 |
| --------------------- | ------------------------------------------- |
| Overview              | Revenue, orders, customers and sales trends |
| Sales Analytics       | Product, category and regional analysis     |
| Customer Intelligence | Customer segmentation                       |
| Sales Forecast        | Experimental sales prediction               |
| Transactions          | Transaction exploration and CSV export      |

## Technology Stack

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Core programming          |
| Pandas       | Data manipulation         |
| NumPy        | Numerical computation     |
| Matplotlib   | Data visualization        |
| Seaborn      | Statistical visualization |
| Plotly       | Interactive charts        |
| Streamlit    | Web dashboard             |
| Scikit-learn | Machine Learning          |
| Pytest       | Unit testing              |

## Project Structure

```text
SalesSense/
│
├── data/
│   └── sales_data.csv
│
├── src/
│   ├── data_preprocessing.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── business_insights.py
│   ├── sales_prediction.py
│   └── customer_segmentation.py
│
├── tests/
│   └── test_preprocessing.py
│
├── assets/
│   └── screenshots/
│
├── app.py
├── generate_data.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

Clone the repository:

```bash
git clone https://github.com/chiragsamaiya05-design/SalesSense.git

cd SalesSense
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Generate the dataset if it is not already available:

```bash
python generate_data.py
```

Run the application:

```bash
streamlit run app.py
```

## Machine Learning

SalesSense implements two Machine Learning approaches.

**1. Customer Segmentation**

* K-Means clustering.
* StandardScaler.
* Customer-level feature engineering.

**2. Sales Forecasting**

* Random Forest Regressor.
* Time-based feature engineering.
* Historical sales features.
* Chronological train-test split.
* MAE, RMSE and R² evaluation.

Note: The current dataset is synthetically generated. Predictions and customer segments are experimental demonstrations, not validated business recommendations.

## Testing

Run unit tests:

```bash
python -m pytest tests/ -v
```

Current preprocessing tests cover:

* Duplicate removal.
* Missing-value handling.
* Date conversion.
* Feature engineering.
* Sales calculation.

## Future Improvements

* Integration with real-world retail datasets.
* Advanced time-series forecasting.
* Customer segmentation evaluation.
* Sales anomaly detection.
* Database integration.
* Improved dashboard filtering.
* Cloud deployment.

## Author

**Chirag Samaiya**

GitHub: https://github.com/chiragsamaiya05-design
