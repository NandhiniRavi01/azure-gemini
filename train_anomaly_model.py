import pandas as pd
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# Simulated historical CPU usage data (Modify as needed)
data = pd.DataFrame({"CPU_Usage": [10, 20, 30, 40, 50, 55, 60, 65, 70, 75, 80, 85, 90]})

# Train StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Train Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
model.fit(scaled_data)

# Save model and scaler
joblib.dump(scaler, "scaler.pkl")
joblib.dump(model, "anomaly_detector.pkl")

print("✅ Model trained with 1 feature (CPU Usage)!")
