import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Sales Trends")

df = pd.read_csv("sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])
st.subheader("📈 Trend Insight")

st.write("""
- Sales fluctuate over time  
- Peaks may indicate seasonal demand  
- Helps identify growth patterns  
""")

trend = df.groupby("Sale_Date")["Sales_Amount"].sum()

fig, ax = plt.subplots()
ax.plot(trend.index, trend.values)

st.pyplot(fig)