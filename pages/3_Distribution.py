import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🧁 Sales Distribution")

# Load data
df = pd.read_csv("sales_data.csv")

# Sidebar filters
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

filtered_df = df[df["Region"] == region]

# Group data
category_sales = filtered_df.groupby("Product_Category")["Sales_Amount"].sum().reset_index()

# Pie chart
fig = px.pie(
    category_sales,
    names="Product_Category",
    values="Sales_Amount",
    title="Sales Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# Download button
st.download_button(
    label="⬇ Download Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_sales.csv",
    mime="text/csv"
)