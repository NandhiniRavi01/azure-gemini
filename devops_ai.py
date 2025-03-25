import google.generativeai as genai
from flask import Flask, request, jsonify

app = Flask(__name__)

# 🔹 Replace with your Google Gemini API Key
GENAI_API_KEY = "AIzaSyCrU3oSpbTid4fAJNoFN948ROPjoqy_WvI"

# 🔹 Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)

def analyze_logs(log_data):
    """Send logs to Google Gemini AI for analysis and get suggested fixes."""
    prompt = f"Analyze the following DevOps log and suggest a fix: {log_data}"
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response.text else "No suggestions available."

@app.route('/jenkins-webhook', methods=['POST'])
def receive_jenkins_logs():
    """Receives logs from Jenkins and returns AI-generated solutions."""
    log_data = request.json.get("logs", "")
    if log_data:
        resolution = analyze_logs(log_data)
        return jsonify({"suggested_fix": resolution}), 200
    return jsonify({"error": "No logs received"}), 400

if __name__ == "__main__":
    app.run(port=5005)

