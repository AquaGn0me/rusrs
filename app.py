from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Configure Gemini API
load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY environment variable set. Please set it before running the app.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def is_sarcastic(text):
    prompt = f"Is the following text sarcastic? Answer 'Yes' or 'No'. Text: '{text}'"
    response = model.generate_content(prompt)
    if response.candidates and response.candidates[0].content.parts:
        return response.candidates[0].content.parts[0].text.strip().lower() == 'yes'
    return False

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/check_sarcasm', methods=['POST'])
def check_sarcasm():
    text = request.form['text']
    sarcastic = is_sarcastic(text)
    # Return JSON response instead of rendering a template
    return jsonify({
        'text': text,
        'sarcastic': sarcastic
    })

if __name__ == '__main__':
    app.run(debug=True)