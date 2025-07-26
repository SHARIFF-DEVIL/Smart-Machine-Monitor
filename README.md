📊 Real-Time Smart Machine Monitoring Dashboard

🚀 Overview

This project simulates a smart industrial environment where multiple machines are monitored in real-time using a Streamlit dashboard. The data is auto-generated and updates live on the dashboard every few seconds, mimicking real-world IoT-enabled factory setups.

🎯 Purpose

To build a real-time, auto-refreshing dashboard that displays the health and status of various industrial machines using simulated IoT data — with no hardware required.

🧠 Key Features

Simulates machine data (temperature, vibration, status)

Real-time data generation using Python

Auto-refreshing Streamlit dashboard

Line charts for temperature and vibration

Status indicators for each machine

🧰 Technologies Used

Python

Streamlit

Pandas

Plotly

CSV (for lightweight simulated storage)

▶️ How to Run

Install Dependencies:

pip install streamlit pandas plotly streamlit-autorefresh

Run the Data Simulator:

python machine_simulator.py

Run the Dashboard:

streamlit run dashboard.py

The dashboard will automatically refresh every 5 seconds to display the latest data.

🌟 Future Enhancements

Add ML-based fault prediction

Integrate MQTT/Firebase for remote updates

Enable user-defined threshold alerts

