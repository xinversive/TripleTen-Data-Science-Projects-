import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("vehicles_us.csv")

st.set_page_config(page_title="Car Sales Dashboard", layout="wide")
st.title("🚗 Car Sales Dashboard")

# Show data checkbox
if st.checkbox("Show Raw Data"):
    st.write(df)

# Price Distribution
st.subheader("Price Distribution")
fig1 = px.histogram(df, x="price")
st.plotly_chart(fig1, use_container_width=True)

# Odometer vs. Price
st.subheader("Price vs. Mileage")
fig2 = px.scatter(df, x="odometer", y="price", color="type")
st.plotly_chart(fig2, use_container_width=True)
