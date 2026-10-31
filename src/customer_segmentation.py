import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def prepare_customer_data(df):

    customer_data = (
        df.groupby("Customer_ID")
        .agg(
            Total_Spending=("Total_Sales", "sum"),
            Total_Orders=("Order_ID", "nunique"),
            Average_Spending=("Total_Sales", "mean"),
            Total_Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    return customer_data

def perform_clustering(customer_data, n_clusters=3):

    features = [
        "Total_Spending",
        "Total_Orders",
        "Average_Spending",
        "Total_Quantity"
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(
        customer_data[features]
    )

    model = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    customer_data["Cluster"] = model.fit_predict(
        scaled_data
    )

    return customer_data, model, scaler


def label_segments(customer_data):

    cluster_spending = (
        customer_data.groupby("Cluster")["Total_Spending"]
        .mean()
        .sort_values()
    )

    labels = {
        cluster_spending.index[0]: "Low Value",
        cluster_spending.index[1]: "Medium Value",
        cluster_spending.index[2]: "High Value"
    }

    customer_data["Segment"] = (
        customer_data["Cluster"].map(labels)
    )

    return customer_data