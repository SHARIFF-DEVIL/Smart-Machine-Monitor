import joblib
import pandas as pd
import os

MODEL_FILE = 'data/trained_model.pkl'

if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError("❌ Trained model not found. Please run model_trainer.py first.")

model = joblib.load(MODEL_FILE)

def predict_health(sensor_row):
    try:
        temperature = float(sensor_row[2])
        vibration = float(sensor_row[3])

        print(f"🧪 Input Temp: {temperature}, Vib: {vibration}")

        features = pd.DataFrame([[temperature, vibration]], columns=['temperature', 'vibration'])

        prediction = int(model.predict(features)[0])
        print(f"🔍 Raw Prediction: {prediction}")

        return prediction

    except Exception as e:
        print(f"❌ Prediction error: {e}")
        return None

if __name__ == "__main__":
    healthy_sample = ['2025-07-26 18:30:00', 'M1', '75.0', '3.2']
    risky_sample = ['2025-07-26 18:31:00', 'M2', '92.4', '4.2']

    result_healthy = predict_health(healthy_sample)
    print(f"Prediction for {healthy_sample[1]}: {'⚠️ At Risk' if result_healthy else '✅ Healthy'}")

    result_risky = predict_health(risky_sample)
    print(f"Prediction for {risky_sample[1]}: {'⚠️ At Risk' if result_risky else '✅ Healthy'}")