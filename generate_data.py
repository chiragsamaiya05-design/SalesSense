
import pandas as pd
import numpy as np

np.random.seed(42)

n = 1000

products = ["Laptop", "Mobile", "Tablet", "Headphones", "Keyboard"]
categories = ["Electronics", "Accessories", "Computers"]
regions = ["North", "South", "East", "West"]
payment_methods = ["UPI", "Credit Card", "Debit Card", "Cash"]

data = {
    "Order_ID": range(1001, 1001 + n),

    "Customer_ID": np.random.randint(101, 300, n),

    "Product": np.random.choice(products, n),

    "Category": np.random.choice(categories, n),

    "Region": np.random.choice(regions, n),

    "Quantity": np.random.randint(1, 6, n),

    "Unit_Price": np.random.randint(500, 50000, n),

    "Payment_Method": np.random.choice(payment_methods, n),

    "Order_Date": pd.date_range(
        start="2025-01-01",
        periods=n,
        freq="D"
    )
}

df = pd.DataFrame(data)

df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

# Introduce missing values for preprocessing practice
df.loc[10:15, "Unit_Price"] = np.nan

# Introduce duplicate records
df = pd.concat([df, df.iloc[:5]], ignore_index=True)

df.to_csv("data/sales_data.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print("Shape:", df.shape)