import streamlit as st
import pandas as pd

st.title("📊 Sales Overview")

# Load data
df = pd.read_csv("sales_data.csv")

# Convert date
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# Sidebar filters
st.sidebar.header("Filters")

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

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", total_sales)
col2.metric("Avg Sales", avg_sales)
col3.metric("Orders", orders)

# Table
st.subheader("Filtered Data")
st.dataframe(filtered_df)