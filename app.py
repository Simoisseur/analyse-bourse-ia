import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(layout="wide")
st.title("🧠 Analyse Long Terme CAC40 + SBF120")

tickers = ["AI.PA", "MC.PA", "ORA.PA", "VIE.PA", "DG.PA"]  # exemples

# Options dans la barre latérale
selected = st.sidebar.selectbox("Choisis une action:", tickers)
period_map = {
    "1 mois": "1mo",
    "3 mois": "3mo",
    "6 mois": "6mo",
    "1 an": "1y",
    "5 ans": "5y",
}
period_label = st.sidebar.selectbox("Période", list(period_map.keys()))
period = period_map[period_label]

# Mise en cache des données pour limiter les appels répétitifs
@st.cache_data(ttl=3600)
def load_data(ticker: str, period: str) -> pd.DataFrame:
    return yf.download(ticker, period=period, interval="1d")

data = load_data(selected, period)

# Calcul de moyennes mobiles simples
data["SMA20"] = data["Close"].rolling(window=20).mean()
data["SMA50"] = data["Close"].rolling(window=50).mean()

st.line_chart(data[["Close", "SMA20", "SMA50"]])

info = yf.Ticker(selected).info
st.subheader("📊 Données fondamentales")
st.write({
    "Nom": info.get("longName"),
    "Secteur": info.get("sector"),
    "PER": info.get("trailingPE"),
    "Rendement dividende": info.get("dividendYield"),
    "Croissance CA 5 ans": info.get("revenueGrowth"),
})
