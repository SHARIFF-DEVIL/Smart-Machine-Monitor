import sqlite3
import pandas as pd
import streamlit as st
import altair as alt

DB_PATH = "data/sensor_data.db"  # Change path if needed

def load_data():
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM sensor_data ORDER BY timestamp DESC LIMIT 100", conn)
        conn.close()
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()

def show_status(df):
    latest = df.iloc[0]
    st.subheader("📟 Machine Status")
    st.metric("Machine ID", latest["machine_id"])
    st.metric("Temperature", f"{latest['temperature']} °C")
    st.metric("Vibration", f"{latest['vibration']} Hz")
    st.metric("Failure Predicted", "❌ Yes" if latest['failure'] else "✅ No")

def show_charts(df):
    st.subheader("📈 Sensor Trends")
    c1, c2 = st.columns(2)

    with c1:
        chart1 = alt.Chart(df).mark_line().encode(
            x='timestamp:T',
            y='temperature:Q',
            color='machine_id:N'
        ).properties(title="Temperature Over Time")
        st.altair_chart(chart1, use_container_width=True)

    with c2:
        chart2 = alt.Chart(df).mark_line().encode(
            x='timestamp:T',
            y='vibration:Q',
            color='machine_id:N'
        ).properties(title="Vibration Over Time")
        st.altair_chart(chart2, use_container_width=True)

def show_logs(df):
    st.subheader("📜 Recent Logs")
    st.dataframe(df.head(10))
