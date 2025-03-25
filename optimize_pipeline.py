import google.generativeai as genai

# 🔹 Replace with your Google Gemini API Key
GENAI_API_KEY = "your_gemini_api_key"

# 🔹 Configure Gemini API
genai.configure(api_key=GENAI_API_KEY)

def optimize_pipeline(job_history):
    """Use AI to suggest CI/CD optimizations for Jenkins."""
    prompt = f"Analyze the following Jenkins job history and suggest optimizations: {job_history}"
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    
    return response.text if response.text else "No optimizations available."

# 🔹 Example Usage
job_history = """
Build #1: Success (3m 45s)
Build #2: Failed - Test Errors (4m 10s)
Build #3: Success (3m 30s)
Build #4: Failed - Memory Leak (5m 20s)
"""

suggestions = optimize_pipeline(job_history)
print("AI Optimization Suggestions:\n", suggestions)

