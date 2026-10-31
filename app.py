import streamlit as st
import pandas as pd
import plotly.express as px

from src.data_preprocessing import load_data, clean_data

st.set_page_config(
    page_title="SalesSense | Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0B1120;
    color: #F8FAFC;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #263244;
}

/* Main headings */
h1, h2, h3 {
    color: #F8FAFC !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background-color: #172235;
    border: 1px solid #26364D;
    padding: 20px;
    border-radius: 12px;
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #94A3B8;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #38BDF8;
}

/* Buttons */
.stButton button {
    border-radius: 8px;
    background-color: #2563EB;
    color: white;
    border: none;
}

/* Dataframe */
div[data-testid="stDataFrame"] {
    border: 1px solid #26364D;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

@st.cache_data
def get_data():

    df = load_data("data/sales_data.csv")

    df = clean_data(df)

    return df


df = get_data()

st.sidebar.title("📊 SalesSense")

st.sidebar.caption("Sales Intelligence Platform")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "NAVIGATION",
    [
        "Overview",
        "Sales Analytics",
        "Customer Intelligence",
        "Sales Forecast",
        "Transactions"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption("SalesSense v1.0")


st.sidebar.subheader("Data Filters")

regions = ["All"] + sorted(df["Region"].unique().tolist())

selected_region = st.sidebar.selectbox(
    "Region",
    regions
)

categories = ["All"] + sorted(df["Category"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Category",
    categories
)

filtered_df = df.copy()

if selected_region != "All":
    filtered_df = filtered_df[
        filtered_df["Region"] == selected_region
    ]

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]



if page == "Overview":

    st.title("Sales Overview")

    st.caption(
        "Monitor your business performance and sales activity."
    )

    st.markdown("---")

    revenue = filtered_df["Total_Sales"].sum()

    orders = filtered_df["Order_ID"].nunique()

    customers = filtered_df["Customer_ID"].nunique()

    aov = revenue / orders if orders else 0

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Revenue",
        f"₹{revenue:,.0f}"
    )

    c2.metric(
        "Total Orders",
        f"{orders:,}"
    )

    c3.metric(
        "Total Customers",
        f"{customers:,}"
    )

    c4.metric(
        "Average Order Value",
        f"₹{aov:,.0f}"
    )

    st.markdown("---")

    left, right = st.columns(2)

    with left:

        product_sales = (
            filtered_df.groupby("Product")["Total_Sales"]
            .sum()
            .reset_index()
            .sort_values("Total_Sales", ascending=False)
        )

        fig = px.bar(
            product_sales,
            x="Product",
            y="Total_Sales",
            title="Revenue by Product",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    with right:

        region_sales = (
            filtered_df.groupby("Region")["Total_Sales"]
            .sum()
            .reset_index()
        )

        fig = px.pie(
            region_sales,
            names="Region",
            values="Total_Sales",
            hole=0.55,
            title="Regional Revenue Distribution",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    monthly = (
        filtered_df.groupby(
            pd.Grouper(key="Order_Date", freq="ME")
        )["Total_Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Order_Date",
        y="Total_Sales",
        markers=True,
        title="Monthly Revenue Trend",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)



elif page == "Sales Analytics":

    st.title("Sales Analytics")

    st.caption("Explore product, category and regional performance.")

    col1, col2 = st.columns(2)

    with col1:

        category = (
            filtered_df.groupby("Category")["Total_Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            category,
            x="Category",
            y="Total_Sales",
            title="Category Performance",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        product = (
            filtered_df.groupby("Product")["Quantity"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            product,
            x="Product",
            y="Quantity",
            title="Product Sales Volume",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)

    region = (
        filtered_df.groupby("Region")["Total_Sales"]
        .sum()
        .reset_index()
    )

    fig = px.bar(
        region,
        x="Region",
        y="Total_Sales",
        title="Regional Performance",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)



elif page == "Customer Intelligence":

    from src.customer_segmentation import (
        prepare_customer_data,
        perform_clustering,
        label_segments
    )

    st.title("Customer Intelligence")

    customer_data = prepare_customer_data(filtered_df)

    customer_data, model, scaler = perform_clustering(
        customer_data,
        n_clusters=3
    )

    customer_data = label_segments(customer_data)

    segment_summary = (
        customer_data.groupby("Segment")
        .agg(
            Customers=("Customer_ID", "count"),
            Revenue=("Total_Spending", "sum")
        )
        .reset_index()
    )

    st.dataframe(
        segment_summary,
        use_container_width=True
    )

    fig = px.scatter(
        customer_data,
        x="Total_Orders",
        y="Total_Spending",
        color="Segment",
        hover_data=["Customer_ID"],
        title="Customer Segmentation",
        template="plotly_dark"
    )

    st.plotly_chart(fig, use_container_width=True)



elif page == "Sales Forecast":

    from src.sales_prediction import (
        prepare_sales_data,
        train_sales_model,
        predict_future_sales
    )

    st.title("Sales Forecast")

    st.info(
        "Forecasts are experimental because the current dataset "
        "contains synthetic sales records."
    )

    days = st.selectbox(
        "Forecast period",
        [7, 15, 30]
    )

    if st.button("Generate Forecast"):

        sales_data = prepare_sales_data(df)

        model, metrics, features = train_sales_model(sales_data)

        future = predict_future_sales(
            model,
            sales_data,
            features,
            days=days
        )

        st.metric("Model MAE", f"₹{metrics['MAE']:,.2f}")

        st.metric("Model R²", f"{metrics['R2 Score']:.3f}")

        fig = px.line(
            future,
            x="Order_Date",
            y="Total_Sales",
            markers=True,
            title=f"Next {days} Days Forecast",
            template="plotly_dark"
        )

        st.plotly_chart(fig, use_container_width=True)


elif page == "Transactions":

    st.title("Sales Transactions")

    search = st.text_input("Search Product")

    transaction_data = filtered_df.copy()

    if search:

        transaction_data = transaction_data[
            transaction_data["Product"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        transaction_data,
        use_container_width=True,
        hide_index=True
    )

    csv = transaction_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "Download Transactions",
        data=csv,
        file_name="sales_transactions.csv",
        mime="text/csv"
    )

