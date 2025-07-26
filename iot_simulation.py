import csv
import random
import time
from datetime import datetime
import os
from predictor import predict_health  # Import prediction function

DATA_FILE = 'data/sensor_data.csv'

# Create CSV file with headers if not exists
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp', 'machine_id', 'temperature', 'vibration', 'health'])

def generate_sensor_data():
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        machine_id = random.choice(['M1', 'M2', 'M3'])

        # Simulate values
        temperature = round(random.uniform(50, 100), 2)
        vibration = round(random.uniform(0.5, 5.0), 2)

        # Predict health using trained model
        health = predict_health([timestamp, machine_id, temperature, vibration])
        health_str = 'At Risk' if health == 1 else 'Healthy'

        data = [timestamp, machine_id, temperature, vibration, health_str]

        # Append to CSV
        with open(DATA_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)

        print(f"Generated: {data}")
        time.sleep(2)

if __name__ == "__main__":
    generate_sensor_data()
