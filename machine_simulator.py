# machine_simulator.py
import pandas as pd
import numpy as np
import time
from datetime import datetime
import os

DATA_PATH = "data/machines.csv"
MACHINES = ["Machine_1", "Machine_2", "Machine_3"]

# Make sure file exists with headers
if not os.path.exists(DATA_PATH):
    pd.DataFrame(columns=["timestamp", "machine_id", "status", "temperature", "vibration"]).to_csv(DATA_PATH, index=False)

def simulate():
    while True:
        rows = []
        for machine in MACHINES:
            status = np.random.choice(["Running", "Idle", "Fault"])
            temp = np.random.normal(loc=70 if status=="Running" else 40, scale=3)
            vibration = np.random.normal(loc=0.3 if status=="Running" else 0.05, scale=0.05)

            rows.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "machine_id": machine,
                "status": status,
                "temperature": round(temp, 2),
                "vibration": round(vibration, 3)
            })

        df = pd.DataFrame(rows)
        df.to_csv(DATA_PATH, mode='a', index=False, header=False)
        print("🟢 Updated Machine Data")
        time.sleep(2)  # Update every 2 seconds

if __name__ == "__main__":
    simulate()
