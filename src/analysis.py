import pandas as pd

def basic_stats(df):


    print("\n========== BASIC STATISTICS ==========")

    print("\nDataset Description:")
    print(df.describe())

    total_revenue = df["Total_Sales"].sum()

    total_orders = df["Order_ID"].nunique()

    total_customers = df["Customer_ID"].nunique()

    average_order_value = total_revenue / total_orders

    print("\nTotal Revenue:", round(total_revenue, 2))
    print("Total Orders:", total_orders)
    print("Total Customers:", total_customers)
    print("Average Order Value:", round(average_order_value, 2))

def product_analysis(df):

    print("\n========== PRODUCT ANALYSIS ==========")

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\nRevenue by Product:")
    print(product_sales)

    return product_sales

def regional_analysis(df):

    region_sales = (
        df.groupby('Region')['Total_Sales'].sum().sort_values(ascending = False)

    )

    print(region_sales)

    return region_sales

def monthly_analysis(df):

    print("\n========== MONTHLY ANALYSIS ==========")

    monthly_sales = (
        df.groupby(["Year", "Month"])["Total_Sales"]
        .sum()
    )

    print(monthly_sales)

    return monthly_sales

def customer_analysis(df):

    print("\n========== CUSTOMER ANALYSIS ==========")

    top_customers = (
        df.groupby("Customer_ID")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    print(top_customers)

    return top_customers

def category_analysis(df):

    print("\n========== CATEGORY ANALYSIS ==========")

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    print(category_sales)

    return category_sales

def run_analysis(df):

    basic_stats(df)

    product_analysis(df)

    regional_analysis(df)

    monthly_analysis(df)

    customer_analysis(df)

    category_analysis(df)