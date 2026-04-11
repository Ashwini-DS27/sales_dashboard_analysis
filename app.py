import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# -------------------------------
# Title
# -------------------------------
st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📊 Sales Dashboard")

# -------------------------------
# File Upload
# -------------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("sales_data.csv")

# -------------------------------
# Data Preprocessing
# -------------------------------
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

# -------------------------------
# Sidebar Filters
# -------------------------------
st.sidebar.header("Filters")

region = st.sidebar.selectbox("Select Region", df["Region"].unique())

date_range = st.sidebar.date_input(
    "Select Date Range",
    [df["Sale_Date"].min(), df["Sale_Date"].max()]
)

# -------------------------------
# Filtering Data
# -------------------------------
filtered_df = df[
    (df["Region"] == region) &
    (df["Sale_Date"] >= pd.to_datetime(date_range[0])) &
    (df["Sale_Date"] <= pd.to_datetime(date_range[1]))
]

# -------------------------------
# KPIs
# -------------------------------
total_sales = int(filtered_df["Sales_Amount"].sum())
avg_sales = int(filtered_df["Sales_Amount"].mean())
orders = filtered_df.shape[0]

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", total_sales)
col2.metric("Avg Sales", avg_sales)
col3.metric("Orders", orders)

# -------------------------------
# Data Table
# -------------------------------
st.subheader("Filtered Data")
st.dataframe(filtered_df)

# -------------------------------
# Revenue by Category
# -------------------------------
st.subheader("Revenue by Category")

category_data = filtered_df.groupby("Product_Category")["Sales_Amount"].sum()

fig1, ax1 = plt.subplots()
category_data.plot(kind="bar", ax=ax1)
st.pyplot(fig1)

# -------------------------------
# Sales Trend
# -------------------------------
st.subheader("Sales Trend")

trend_data = filtered_df.groupby("Sale_Date")["Sales_Amount"].sum()

fig2, ax2 = plt.subplots()
trend_data.plot(ax=ax2)
st.pyplot(fig2)

# -------------------------------
# Sales Distribution
# -------------------------------
st.subheader("Sales Distribution")

fig3, ax3 = plt.subplots()
category_data.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
st.pyplot(fig3)

# -------------------------------
# ML MODEL (Prediction)
# -------------------------------
st.subheader("🔮 Predict Future Sales")

# Convert date to numeric
df["Days"] = (df["Sale_Date"] - df["Sale_Date"].min()).dt.days

X = df[["Days"]]
y = df["Sales_Amount"]

model = LinearRegression()
model.fit(X, y)

future_days = st.slider("Select days ahead", 1, 365, 30)

prediction = model.predict(np.array([[future_days]]))

st.success(f"Predicted Sales after {future_days} days: {prediction[0]:.2f}")
