import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🍩 Sales Distribution")

df = pd.read_csv("sales_data.csv")

category = df["Product_Category"].value_counts()

fig, ax = plt.subplots()
ax.pie(category, labels=category.index, autopct="%1.1f%%")

st.pyplot(fig)