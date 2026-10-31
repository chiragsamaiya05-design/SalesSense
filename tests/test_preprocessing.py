import pandas as pd

from src.data_preprocessing import clean_data


def test_duplicate_removal():

    df = pd.DataFrame({
        "Order_ID": [1, 2, 2],
        "Customer_ID": [101, 102, 102],
        "Product": ["Laptop", "Mobile", "Mobile"],
        "Category": ["Electronics"] * 3,
        "Region": ["North"] * 3,
        "Quantity": [2, 1, 1],
        "Unit_Price": [1000, 500, 500],
        "Payment_Method": ["UPI"] * 3,
        "Order_Date": [
            "2025-01-01",
            "2025-01-02",
            "2025-01-02"
        ]
    })

    cleaned = clean_data(df)

    assert len(cleaned) == 2


def test_missing_values():

    df = pd.DataFrame({
        "Order_ID": [1, 2],
        "Customer_ID": [101, 102],
        "Product": ["Laptop", "Mobile"],
        "Category": ["Electronics", "Electronics"],
        "Region": ["North", "South"],
        "Quantity": [2, 1],
        "Unit_Price": [1000, None],
        "Payment_Method": ["UPI", "Cash"],
        "Order_Date": ["2025-01-01", "2025-01-02"]
    })

    cleaned = clean_data(df)

    assert cleaned["Unit_Price"].isnull().sum() == 0


def test_date_conversion():

    df = pd.DataFrame({
        "Order_ID": [1],
        "Customer_ID": [101],
        "Product": ["Laptop"],
        "Category": ["Electronics"],
        "Region": ["North"],
        "Quantity": [2],
        "Unit_Price": [1000],
        "Payment_Method": ["UPI"],
        "Order_Date": ["2025-01-01"]
    })

    cleaned = clean_data(df)

    assert pd.api.types.is_datetime64_any_dtype(
        cleaned["Order_Date"]
    )

def test_feature_engineering():

    df = pd.DataFrame({
        "Order_ID": [1],
        "Customer_ID": [101],
        "Product": ["Laptop"],
        "Category": ["Electronics"],
        "Region": ["North"],
        "Quantity": [2],
        "Unit_Price": [1000],
        "Payment_Method": ["UPI"],
        "Order_Date": ["2025-03-15"]
    })

    cleaned = clean_data(df)

    assert "Month" in cleaned.columns
    assert "Year" in cleaned.columns
    assert "Day" in cleaned.columns

    assert cleaned.iloc[0]["Month"] == 3
    assert cleaned.iloc[0]["Year"] == 2025
    assert cleaned.iloc[0]["Day"] == 15


def test_sales_calculation():

    df = pd.DataFrame({
        "Order_ID": [1],
        "Customer_ID": [101],
        "Product": ["Laptop"],
        "Category": ["Electronics"],
        "Region": ["North"],
        "Quantity": [3],
        "Unit_Price": [2000],
        "Payment_Method": ["UPI"],
        "Order_Date": ["2025-01-01"]
    })

    cleaned = clean_data(df)

    expected_sales = 3 * 2000

    assert cleaned.iloc[0]["Total_Sales"] == expected_sales

