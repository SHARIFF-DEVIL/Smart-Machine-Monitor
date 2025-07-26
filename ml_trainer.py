import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

DATA_FILE = 'data/sensor_data.csv'
MODEL_FILE = 'data/trained_model.pkl'

def generate_labels(df):
    df['label'] = ((df['temperature'] > 85) | (df['vibration'] > 4.0)).astype(int)
    return df

def train_model():
    if not os.path.exists(DATA_FILE):
        print("❌ Sensor data file not found!")
        return

    df = pd.read_csv(DATA_FILE)
    df.dropna(inplace=True)

    df = generate_labels(df)

    # Show class balance
    print("Class Distribution:\n", df['label'].value_counts())

    X = df[['temperature', 'vibration']]
    y = df['label']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    model = RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced')
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print("✅ Model Trained Successfully")
    print("📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, MODEL_FILE)
    print(f"💾 Model saved to {MODEL_FILE}")

if __name__ == "__main__":
    train_model()
