# dashboard.py

import streamlit as st
import pandas as pd
import time
from datetime import datetime, timedelta
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

DATA_PATH = "data/machines.csv"
REFRESH_INTERVAL = 5  # seconds

# Refresh every REFRESH_INTERVAL seconds
st_autorefresh(interval=REFRESH_INTERVAL * 1000, key="datarefresh")

st.set_page_config(page_title="Smart Machine Monitor", layout="wide")

st.title("🛠️ Smart Machine Monitor Dashboard")
st.markdown("Real-time updates of machine statuses and sensor readings.")

# Load Data
@st.cache_data(ttl=REFRESH_INTERVAL)
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

if df.empty:
    st.warning("Waiting for machine data...")
    st.stop()

# Convert and filter timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'])
df = df[df['timestamp'] >= datetime.now() - timedelta(minutes=5)]

latest_df = df.sort_values('timestamp').groupby('machine_id').tail(1)

# KPI Cards
st.subheader("⚙️ Machine Overview")
kpi_cols = st.columns(len(latest_df))
for i, (_, row) in enumerate(latest_df.iterrows()):
    with kpi_cols[i]:
        st.metric(
            label=f"{row['machine_id']}",
            value=row["status"],
            delta=f"Temp: {row['temperature']}°C | Vib: {row['vibration']}"
        )

st.divider()

# Time Series Charts
st.subheader("📈 Sensor Trends (Last 5 minutes)")
tab1, tab2 = st.tabs(["🌡 Temperature", "📳 Vibration"])

with tab1:
    fig = px.line(df, x="timestamp", y="temperature", color="machine_id", markers=True,
                  title="Temperature Over Time")
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    fig2 = px.line(df, x="timestamp", y="vibration", color="machine_id", markers=True,
                   title="Vibration Over Time")
    st.plotly_chart(fig2, use_container_width=True)

st.caption("🔄 Dashboard auto-updates every 5 seconds.")
