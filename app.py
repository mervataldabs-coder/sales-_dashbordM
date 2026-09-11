
import pandas as pd
import plotly.express as px 
import streamlit as st



st.set_page_config(
    page_title="Sales Dashboard"
,
    page_icon="📊",
    layout="wide",
)
@st.cache_data
def load_data():
   
    df = pd.read_csv
    ("Sales_Data_Large_2.csv")

    df["Totalsales"] = df["UnitPrice"] * df["Quantity"]
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month

    return df



