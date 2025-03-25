import os
import joblib
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import numpy as np

# Define file paths
model_path = "anomaly_detector.pkl"
scaler_path = "scaler.pkl"

# Check if model files exist
if os.path.exists(model_path) and os.path.exists(scaler_path):
    print("📂 Loading existing model and scaler...")
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
else:
    print("🚀 No existing model found. Training a new one...")

    # Generate random training data (Replace this with real data)
    X_train = np.random.rand(100, 5)

    # Standardize the data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Train an Isolation Forest model
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X_train_scaled)

    # Save the trained model
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    print(f"✅ Model saved successfully: {model_path}, {scaler_path}")
