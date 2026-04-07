import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_page_config(page_title="Sales Dashboard", layout="wide")
df = pd.read_csv("sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0e1117;
    color: white;
}
[data-testid="stMetric"] {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)
st.title("Sales Dashboard")

col1, col2 = st.columns(2)

with col1:
    region_selected = st.selectbox("Select Region", df["Region"].unique())

with col2:
    date_range = st.date_input("Select Date Range",
                              [df["Sale_Date"].min(), df["Sale_Date"].max()])

filtered_df = df[
    (df["Region"] == region_selected) &
    (df["Sale_Date"] >= pd.to_datetime(date_range[0])) &
    (df["Sale_Date"] <= pd.to_datetime(date_range[1]))
]
total_sales = filtered_df["Sales_Amount"].sum()
avg_sales = filtered_df["Sales_Amount"].mean()
orders = filtered_df.shape[0]

st.markdown("## Overview")

c1, c2, c3 = st.columns(3)
c1.metric("Total Sales", f"{total_sales:,.0f}")
c2.metric("Avg Sales", f"{avg_sales:,.0f}")
c3.metric("Orders", orders)

st.markdown("---")
st.subheader("Filtered Data")
st.dataframe(filtered_df)
st.subheader("Revenue by Category")

chart_data = filtered_df.groupby("Product_Category")["Sales_Amount"].sum()

plt.figure(figsize=(6,4))
plt.bar(chart_data.index, chart_data.values)
plt.xticks(rotation=30)
plt.title("Revenue by Category")
plt.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(plt)
st.subheader("Sales Trend")
trend_data = filtered_df.groupby("Sale_Date")["Sales_Amount"].sum()
st.line_chart(trend_data)
st.subheader("Sales Distribution")

fig, ax = plt.subplots()
ax.pie(chart_data.values, labels=chart_data.index, autopct="%1.1f%%")
ax.axis("equal")

st.pyplot(fig)