import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Sample log data (Replace with real logs)
data = pd.DataFrame({"CPU_Usage": [20, 21, 19, 22, 50, 80, 85, 22, 23, 21]})

# Train Isolation Forest model
model = IsolationForest(contamination=0.2)
model.fit(data)

# Save model
joblib.dump(model, "anomaly_detector.pkl")

