import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

def prepare_sales_data(df):

    daily_sales = (
        df.groupby("Order_Date")["Total_Sales"]
        .sum()
        .reset_index()
    )

    daily_sales = daily_sales.sort_values("Order_Date")

    daily_sales["Day"] = daily_sales["Order_Date"].dt.day

    daily_sales["Month"] = daily_sales["Order_Date"].dt.month

    daily_sales["DayOfWeek"] = daily_sales["Order_Date"].dt.dayofweek

    daily_sales["DayOfYear"] = daily_sales["Order_Date"].dt.dayofyear

    daily_sales["TimeIndex"] = np.arange(len(daily_sales))

    # Historical sales features
    daily_sales["Previous_Day_Sales"] = (
        daily_sales["Total_Sales"].shift(1)
    )

    daily_sales["Previous_7_Days_Sales"] = (
        daily_sales["Total_Sales"].shift(7)
    )

    daily_sales = daily_sales.dropna().reset_index(drop=True)

    return daily_sales

def train_sales_model(data):

    features = [
        "Day",
        "Month",
        "DayOfWeek",
        "DayOfYear",
        "TimeIndex",
        "Previous_Day_Sales",
        "Previous_7_Days_Sales"
    ]

    X = data[features]

    y = data["Total_Sales"]

    # Chronological train-test split
    split = int(len(data) * 0.8)

    X_train = X.iloc[:split]
    X_test = X.iloc[split:]

    y_train = y.iloc[:split]
    y_test = y.iloc[split:]

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    r2 = r2_score(y_test, predictions)

    metrics = {
        "MAE": mae,
        "RMSE": rmse,
        "R2 Score": r2
    }

    return model, metrics, features


def predict_future_sales(model, data, features, days=30):

    history = data.copy()

    future_predictions = []

    for _ in range(days):

        last_row = history.iloc[-1]

        next_date = last_row["Order_Date"] + pd.Timedelta(days=1)

        new_row = {
            "Order_Date": next_date,
            "Day": next_date.day,
            "Month": next_date.month,
            "DayOfWeek": next_date.dayofweek,
            "DayOfYear": next_date.dayofyear,
            "TimeIndex": len(history),
            "Previous_Day_Sales": history.iloc[-1]["Total_Sales"],
            "Previous_7_Days_Sales": history.iloc[-7]["Total_Sales"]
        }

        input_data = pd.DataFrame([new_row])[features]

        predicted_sales = model.predict(input_data)[0]

        new_row["Total_Sales"] = max(0, predicted_sales)

        future_predictions.append(new_row)

        history = pd.concat(
            [history, pd.DataFrame([new_row])],
            ignore_index=True
        )

    return pd.DataFrame(future_predictions)