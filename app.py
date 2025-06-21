import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")
st.title("🧠 Analyse Long Terme CAC40 + SBF120")

tickers = ["AI.PA", "MC.PA", "ORA.PA", "VIE.PA", "DG.PA"]  # exemples

selected = st.selectbox("Choisis une action:", tickers)
data = yf.download(selected, period="1y", interval="1d")
st.line_chart(data["Close"])

info = yf.Ticker(selected).info
st.subheader("📊 Données fondamentales")
st.write({
    "Nom": info.get("longName"),
    "Secteur": info.get("sector"),
    "PER": info.get("trailingPE"),
    "Rendement dividende": info.get("dividendYield"),
    "Croissance CA 5 ans": info.get("revenueGrowth"),
})
