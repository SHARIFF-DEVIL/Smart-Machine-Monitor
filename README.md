# 🏭 5G-Enabled Federated Learning for Real-Time Predictive Maintenance in Smart Factories

A smart industry simulation project that combines **5G, IoT, Federated Learning**, and **real-time dashboards** to detect machine failures before they occur — without using real hardware.

---

## 🚀 Project Overview

This project simulates a modern Industry 4.0 factory floor with:
- Multiple machines sending sensor data (e.g., temperature, vibration).
- Real-time predictions on failure risk using **Federated Learning (FL)**.
- Live updating dashboard using **Streamlit**.
- Simulated network delays over **5G/WiFi**.

> 📡 Built to demonstrate **edge-to-cloud ML processing** and predictive maintenance with **zero hardware**, ideal for research, IEEE publications, and academic demos.

---

## 🧠 Features

- ✅ Simulated **IoT Sensor Data** from multiple machines.
- 🔁 **Federated Learning** for distributed model training.
- 🌐 Simulated **5G and WiFi network** delays.
- 📊 **Live Streamlit dashboard** with machine status and predictions.
- 🔔 Real-time failure risk alerts (e.g., 🔴 Risky / 🟢 Safe).
- 📦 Modular Python codebase with separate modules for each functionality.

---

## 📂 Folder Structure

5G_Federated_Predictive_Maintenance/
├── iot_simulator.py # Generates live IoT sensor data
├── network_simulator.py # Adds simulated 5G/WiFi latency
├── ml_trainer.py # Trains model (with optional FL logic)
├── predictor.py # Predicts failure from live sensor data
├── dashboard.py # Real-time Streamlit dashboard
├── requirements.txt # Python dependencies
├── README.md # You're here!
└── data/
├── sensor_data.csv # Training data
└── trained_model.pkl # Serialized ML model
