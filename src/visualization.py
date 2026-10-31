import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

sns.set_theme(style="whitegrid")

def product_sales_chart(df):

    product_sales = (
        df.groupby("Product")["Total_Sales"]
        .sum()
        .sort_values(ascending=False)
    )

    plt.figure(figsize=(10, 5))

    sns.barplot(
        x=product_sales.index,
        y=product_sales.values
    )

    plt.title("Revenue by Product")
    plt.xlabel("Product")
    plt.ylabel("Revenue")

    plt.tight_layout()
    plt.show()


def category_sales_chart(df):

    category_sales = (
        df.groupby("Category")["Total_Sales"]
        .sum()
    )

    plt.figure(figsize=(8, 8))

    plt.pie(
        category_sales,
        labels=category_sales.index,
        autopct="%1.1f%%",
        startangle=90
    )

    plt.title("Category-wise Revenue Distribution")

    plt.show()


def monthly_sales_chart(df):

    monthly_sales = (
        df.groupby("Order_Date")["Total_Sales"]
        .sum()
        .resample("ME")
        .sum()
    )

    plt.figure(figsize=(12, 5))

    plt.plot(
        monthly_sales.index,
        monthly_sales.values,
        marker="o"
    )

    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")

    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def regional_sales_chart(df):

    region_sales = (
        df.groupby("Region")["Total_Sales"]
        .sum()
        .sort_values()
    )

    plt.figure(figsize=(9, 5))

    sns.barplot(
        x=region_sales.values,
        y=region_sales.index,
        orient="h"
    )

    plt.title("Regional Sales Performance")
    plt.xlabel("Revenue")
    plt.ylabel("Region")

    plt.tight_layout()
    plt.show()


def correlation_heatmap(df):

    numerical_df = df.select_dtypes(include="number")

    correlation = numerical_df.corr()

    plt.figure(figsize=(10, 7))

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Sales Data Correlation Heatmap")

    plt.tight_layout()
    plt.show()



def interactive_sales_chart(df):

    fig = px.scatter(
        df,
        x="Quantity",
        y="Total_Sales",
        color="Category",
        hover_data=["Product", "Region"],
        title="Quantity vs Total Sales"
    )

    fig.show()


def run_visualizations(df):

    product_sales_chart(df)

    category_sales_chart(df)

    monthly_sales_chart(df)

    regional_sales_chart(df)

    correlation_heatmap(df)

    interactive_sales_chart(df)