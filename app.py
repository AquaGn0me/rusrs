from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Configure Gemini API - Replace with your actual API key

load_dotenv()

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY environment variable set. Please set it before running the app.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def is_sarcastic(text):
    prompt = f""""

    You are an advanced AI trained to analyze text for sarcasm. Your task is to evaluate 
    an entire block of text, identify any portions that might be sarcastic, and analyze them.

    Definition of Sarcasm: Sarcasm is a form of verbal irony where a speaker conveys the 
    opposite of their literal meaning, often in a mocking or exaggerated tone.
    Carefully consider the tone, word choice, punctuation, and the broader context of the text.
    Look for clues such as hyperbole, incongruity between literal meaning and context, 
    and the presence of humor or criticism.
    Your response should include:
    A list of parts of the block that may be sarcastic.
    For each part, a determination of whether it is sarcastic (yes or no), 
    your confidence percentage (0-100%), and a brief explanation justifying your analysis.
    Here is the format for your output:

    Detected Sarcastic Parts:
    "[Potential sarcastic part]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage]
    Explanation: [Analysis of why this part may or may not be sarcastic.]
    "[Next potential sarcastic part]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage]
    Explanation: [Analysis of why this part may or may not be sarcastic.]
    If no sarcasm is detected, state clearly: "No sarcasm detected in the block of text."

    Here is the text: {text}

    Review your analysis of the block of text for coherence and depth. 
    Ensure you have thoroughly examined all portions of the text for possible 
    sarcasm and that your justifications reference specific elements like tone, 
    word choice, punctuation, or context.

    If there is ambiguity in whether a part is sarcastic, explain both sides 
    of the interpretation and adjust the confidence level to reflect the uncertainty.
    Double-check that all sarcastic elements have been identified and that the analysis 
    aligns with typical patterns of sarcasm in human communication.
    """
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
    return render_template('result.html', text=text, sarcastic=sarcastic)

if __name__ == '__main__':
    app.run(debug=True)
