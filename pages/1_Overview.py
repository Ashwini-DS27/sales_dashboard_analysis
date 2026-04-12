import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Overview")
st.subheader("📌 Key Insights")

top_product = df.groupby("Product_Category")["Sales_Amount"].sum().idxmax()
top_region = df.groupby("Region")["Sales_Amount"].sum().idxmax()

st.write(f"🏆 Top Performing Category: {top_product}")
st.write(f"🌍 Top Region: {top_region}")
st.write("📈 Sales show fluctuating trends over time")

df = pd.read_csv("sales_data.csv")

# Revenue by category
category_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

fig, ax = plt.subplots()
ax.bar(category_sales.index, category_sales.values)

st.pyplot(fig)