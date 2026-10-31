# SalesSense – Sales Analytics & Predictive Intelligence

An interactive sales analytics application built using Python, Pandas, NumPy, Plotly, Streamlit and Scikit-learn.

## Overview

SalesSense helps businesses analyze sales transactions, monitor revenue performance, identify business trends and experiment with predictive sales forecasting.

## Features

* Sales performance monitoring
* Revenue and order analytics
* Product-wise sales analysis
* Regional performance analysis
* Customer analytics
* Data preprocessing and cleaning
* Interactive Streamlit dashboard
* Automated business insights
* Experimental 30-day sales forecasting
* CSV report export

## Technology Stack

| Technology   | Usage                     |
| ------------ | ------------------------- |
| Python       | Core programming          |
| Pandas       | Data manipulation         |
| NumPy        | Numerical operations      |
| Matplotlib   | Data visualization        |
| Seaborn      | Statistical visualization |
| Plotly       | Interactive charts        |
| Streamlit    | Dashboard                 |
| Scikit-learn | Machine Learning          |
| Pytest       | Unit testing              |

## Project Structure

```text
SalesSense/
├── data/
├── src/
├── tests/
├── app.py
├── generate_data.py
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd SalesSense
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the dataset:

```bash
python generate_data.py
```

Run the application:

```bash
streamlit run app.py
```

## Machine Learning

SalesSense uses a Random Forest Regressor to experiment with daily sales forecasting.

Model evaluation metrics:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

The generated dataset is synthetic, so forecasting results are intended for experimentation rather than real-world business decisions.

## Future Improvements

* Real-world retail datasets
* Advanced time-series forecasting
* Customer segmentation using clustering
* Sales anomaly detection
* Database integration
* User authentication
* Cloud deployment

## Author

Chirag Samaiya
