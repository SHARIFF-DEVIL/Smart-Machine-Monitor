import sqlite3
import os

DB_FILE = 'data/machine_data.db'

def init_db():
    """Creates the database and logs table if not exists."""
    if not os.path.exists('data'):
        os.makedirs('data')

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            machine_id TEXT,
            temperature REAL,
            vibration REAL,
            prediction INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def insert_log(timestamp, machine_id, temperature, vibration, prediction):
    """Inserts a new row into the logs table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO logs (timestamp, machine_id, temperature, vibration, prediction)
        VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, machine_id, temperature, vibration, prediction))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    # Example test
    insert_log("2025-07-26 18:32:00", "M2", 78.6, 3.1, 0)
    print("✅ Sample log inserted.")
