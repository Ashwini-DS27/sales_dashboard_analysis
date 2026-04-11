import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = pd.read_csv("sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# Sidebar filters
st.sidebar.title("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Sale_Date"].min(), df["Sale_Date"].max()]
)

# Filter data
filtered_df = df[
    (df["Region"] == region) &
    (df["Sale_Date"] >= pd.to_datetime(date_range[0])) &
    (df["Sale_Date"] <= pd.to_datetime(date_range[1]))
]

# Metrics
total_sales = int(filtered_df["Sales_Amount"].sum())
avg_sales = int(filtered_df["Sales_Amount"].mean())
orders = filtered_df.shape[0]

# UI
st.title("📊 Sales Dashboard")

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", total_sales)
col2.metric("Avg Sales", avg_sales)
col3.metric("Orders", orders)

st.subheader("Filtered Data")
st.dataframe(filtered_df)