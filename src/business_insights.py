def generate_insights(df):

    insights = []

    # Total revenue
    total_revenue = df["Total_Sales"].sum()

    # Best-selling product by revenue
    product_sales = df.groupby("Product")["Total_Sales"].sum()

    best_product = product_sales.idxmax()

    # Lowest-performing product by revenue
    worst_product = product_sales.idxmin()

    # Best-performing region
    region_sales = df.groupby("Region")["Total_Sales"].sum()

    best_region = region_sales.idxmax()

    # Best-performing category
    category_sales = df.groupby("Category")["Total_Sales"].sum()

    best_category = category_sales.idxmax()

    # Average order value
    average_order = df.groupby("Order_ID")["Total_Sales"].sum().mean()

    insights.append(
        f"Total revenue generated: ₹{total_revenue:,.2f}"
    )

    insights.append(
        f"Highest revenue product: {best_product}"
    )

    insights.append(
        f"Lowest revenue product: {worst_product}"
    )

    insights.append(
        f"Best performing region: {best_region}"
    )

    insights.append(
        f"Top revenue category: {best_category}"
    )

    insights.append(
        f"Average Order Value: ₹{average_order:,.2f}"
    )

    return insights