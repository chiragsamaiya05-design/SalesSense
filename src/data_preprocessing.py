import pandas as pd

def load_data(path):
    df = pd.read_csv(path)

    return df


def inspect_data(df):
    print("\nDataset Information:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

def clean_data(df):

    df = df.drop_duplicates()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    df["Unit_Price"] = df["Unit_Price"].fillna(
        df["Unit_Price"].median()
    )

    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

    df["Month"] = df["Order_Date"].dt.month

    df["Year"] = df["Order_Date"].dt.year

    df["Day"] = df["Order_Date"].dt.day

    print("\nData cleaning completed!")

    return df

