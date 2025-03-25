import pandas as pd
import joblib
import time
import psutil
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load model & scaler
model = joblib.load("anomaly_detector.pkl")
scaler = joblib.load("scaler.pkl")

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = os.getenv("SENDER_EMAIL")  # Use .env file for security
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")  # Use app password
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

def send_email(cpu_usage):
    """Send an email alert if an anomaly is detected."""
    subject = "⚠️ Anomaly Detected in CPU Usage!"
    body = f"Alert! Anomalous CPU usage detected: {cpu_usage}%"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print(f"📧 Alert email sent successfully for CPU Usage: {cpu_usage}%")
    except Exception as e:
        print(f"❌ Error sending email: {e}")

# Continuous Monitoring
print("🚀 Monitoring CPU usage for anomalies...")
while True:
    # Get real-time CPU usage
    new_cpu_usage = psutil.cpu_percent(interval=1)  # Gets CPU usage in %

    # Format data
    new_data = pd.DataFrame({"CPU_Usage": [new_cpu_usage]})
    new_data_scaled = scaler.transform(new_data)

    # Predict anomalies
    prediction = model.predict(new_data_scaled)
    
    # Print status
    if prediction[0] == -1:
        print(f"🚨 Anomaly detected! CPU Usage: {new_cpu_usage}%")
        send_email(new_cpu_usage)
    else:
        print(f"✅ Normal CPU usage: {new_cpu_usage}%")

    time.sleep(5)  # Wait before checking again
