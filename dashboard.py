import streamlit as st
import pandas as pd
import sqlite3
import time

DB_FILE = 'data/machine_data.db'

st.set_page_config(page_title="Smart Factory Dashboard", layout="wide")

def load_data():
    conn = sqlite3.connect(DB_FILE)
    query = "SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100"
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def show_status(df):
    st.subheader("📊 Machine Status")
    latest = df.groupby('machine_id').first().reset_index()
    for _, row in latest.iterrows():
        color = "green" if row['prediction'] == 1 else "red"
        status = "✅ Healthy" if row['prediction'] == 1 else "⚠️ At Risk"
        st.markdown(f"""
            <div style='padding:10px; border-radius:10px; background-color:{color}; color:white; margin-bottom:10px;'>
                <strong>{row['machine_id']}</strong>: {status}<br>
                Temp: {row['temperature']}°C | Vib: {row['vibration']} m/s²<br>
                Last Updated: {row['timestamp']}
            </div>
        """, unsafe_allow_html=True)

def show_charts(df):
    st.subheader("📈 Sensor Trends")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    machines = df['machine_id'].unique()

    for machine in machines:
        st.markdown(f"### {machine}")
        mdf = df[df['machine_id'] == machine].sort_values('timestamp')

        col1, col2 = st.columns(2)
        with col1:
            st.line_chart(mdf.set_index('timestamp')['temperature'], use_container_width=True)
        with col2:
            st.line_chart(mdf.set_index('timestamp')['vibration'], use_container_width=True)

def show_logs(df):
    st.subheader("🧾 Recent Logs")
    st.dataframe(df, use_container_width=True)

def main():
    st.title("🛠️ 5G + IoT + ML Smart Factory Dashboard")

    refresh_interval = st.sidebar.slider("⏱️ Refresh every (seconds)", 2, 20, 5)
    st.sidebar.markdown("Built with ❤️ using Streamlit + SQLite + ML")

    placeholder = st.empty()

    while True:
        with placeholder.container():
            df = load_data()
            if df.empty:
                st.warning("No data available yet. Please start the simulator.")
            else:
                show_status(df)
                show_charts(df)
                show_logs(df)

        time.sleep(refresh_interval)
        st.experimental_rerun()  # Refresh the dashboard

if __name__ == "__main__":
    main()
