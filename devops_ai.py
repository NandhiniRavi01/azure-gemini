import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Replace with your Google Gemini API Key
GENAI_API_KEY = "AIzaSyC5EAlxy8hY6fiiOrk74S3E13fkI0U8KqU"

# 🔹 Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)

def analyze_logs(log_data):
    """Send logs to Google Gemini AI for analysis and get suggested fixes."""
    prompt = f"Analyze the following DevOps log and suggest a fix: {log_data}"
    
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    response = model.generate_content(prompt)
    
    return response.text if response.text else "No suggestions available."

@app.route("/", methods=["GET"])
def home():
    """Home route to verify API is running."""
    return jsonify({"message": "DevOps AI API is running!"}), 200

@app.route('/jenkins-webhook', methods=['POST'])
def receive_jenkins_logs():
    """Receives logs from Jenkins and returns AI-generated solutions."""
    log_data = request.json.get("logs", "")
    if log_data:
        resolution = analyze_logs(log_data)
        return jsonify({"suggested_fix": resolution}), 200
    return jsonify({"error": "No logs received"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)
