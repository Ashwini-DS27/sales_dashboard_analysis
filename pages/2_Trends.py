import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Sales Trends")

# Load data
df = pd.read_csv("sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Sale_Date"].min(), df["Sale_Date"].max()]
)

# Filter
filtered_df = df[
    (df["Region"] == region) &
    (df["Sale_Date"] >= pd.to_datetime(date_range[0])) &
    (df["Sale_Date"] <= pd.to_datetime(date_range[1]))
]

# Group data
trend_data = filtered_df.groupby("Sale_Date")["Sales_Amount"].sum().reset_index()

# Plot
fig = px.line(trend_data, x="Sale_Date", y="Sales_Amount", title="Sales Trend")

st.plotly_chart(fig, use_container_width=True)