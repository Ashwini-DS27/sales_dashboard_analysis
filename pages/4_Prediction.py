import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("🔮 Sales Prediction")

df = pd.read_csv("sales_data.csv")
df["Sale_Date"] = pd.to_datetime(df["Sale_Date"])

df_sorted = df.sort_values("Sale_Date")
df_sorted["Date_Ordinal"] = df_sorted["Sale_Date"].map(pd.Timestamp.toordinal)

X = df_sorted[["Date_Ordinal"]]
y = df_sorted["Sales_Amount"]

model = LinearRegression()
model.fit(X, y)

future_days = st.slider("Select days ahead", 1, 30, 7)

future_dates = np.array([
    df_sorted["Date_Ordinal"].max() + i for i in range(1, future_days+1)
]).reshape(-1,1)

predictions = model.predict(future_dates)

st.write(f"📊 Predicted sales for next {future_days} days:")
st.write(predictions)