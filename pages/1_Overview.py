import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Overview")
df = pd.read_csv("sales_data.csv")
st.subheader("📊 Business Summary")

st.write("""
- Sales show variation across categories and regions  
- Certain products contribute more to revenue  
- Trends indicate changing demand over time  
""")

# Revenue by category
category_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

fig, ax = plt.subplots()
ax.bar(category_sales.index, category_sales.values)

st.pyplot(fig)