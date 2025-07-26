import time
import random
import csv
from datetime import datetime
import os

from predictor import predict_health
from db_handler import insert_log

DATA_FILE = 'data/sensor_data.csv'
ENRICHED_FILE = 'data/enriched_sensor_data.csv'  # Optional new file with health status

def simulate_5g_network_delay():
    """Simulates 5G network latency (1ms to 50ms)."""
    delay = random.uniform(0.001, 0.05)
    time.sleep(delay)
    return delay

def stream_data():
    print("🔄 Starting network simulator...")
    last_line = 0

    # Create enriched file if not exists
    if not os.path.exists(ENRICHED_FILE):
        with open(ENRICHED_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'machine_id', 'temperature', 'vibration', 'health'])

    while True:
        if not os.path.exists(DATA_FILE):
            print("❌ Sensor data file not found.")
            time.sleep(2)
            continue

        with open(DATA_FILE, 'r') as file:
            lines = file.readlines()

        # Skip the header and already processed lines
        new_data = lines[last_line + 1:]

        for row in new_data:
            fields = row.strip().split(',')
            if len(fields) != 4:
                continue  # Skip malformed rows

            timestamp, machine_id, temperature, vibration = fields

            # Simulate 5G delay
            delay = simulate_5g_network_delay()

            # Predict machine health
            prediction = predict_health(fields)
            health_status = 'At Risk' if prediction else 'Healthy'

            # Log to SQL database
            insert_log(timestamp, machine_id, float(temperature), float(vibration), prediction)

            # Append enriched data
            with open(ENRICHED_FILE, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, machine_id, temperature, vibration, health_status])

            # Print status
            print(f"[{timestamp}] Delay: {round(delay * 1000, 2)} ms → "
                  f"{machine_id}: Temp={temperature}°C, Vib={vibration} m/s² → {'⚠️ At Risk' if prediction else '✅ Healthy'}")

        # Update pointer to last line processed
        last_line = len(lines) - 1
        time.sleep(1)

if __name__ == "__main__":
    stream_data()
