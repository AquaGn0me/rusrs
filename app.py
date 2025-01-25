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

def get_sarcasm_analysis(text):
    prompt = f""""
    You are an advanced AI trained to analyze text for sarcasm, sentence by sentence.
    For each sentence in the input text, determine if it is sarcastic or not.

    Definition of Sarcasm: Sarcasm is a form of verbal irony where a speaker conveys the 
    opposite of their literal meaning, often in a mocking or exaggerated tone.

    Analyze each sentence individually, considering tone, word choice, and context within the sentence.
    Your response should be structured as follows:

    Sentence 1: "[Sentence 1]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage 0-100]
    Explanation: [Brief explanation for sentence 1]

    Sentence 2: "[Sentence 2]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage 0-100]
    Explanation: [Brief explanation for sentence 2]

    ... and so on for each sentence in the input text.

    If no sarcasm is detected in a sentence, the explanation can be brief, like "No sarcasm detected."

    Input Text:
    {text}

    Ensure your analysis is sentence-specific and follows the requested format for each sentence.
    Provide a confidence level for each determination to indicate the certainty of your analysis.
    """
    response = model.generate_content(prompt)
    if response.candidates and response.candidates[0].content.parts:
        raw_analysis = response.candidates[0].content.parts[0].text.strip()
        sentence_analyses = []
        sentences = raw_analysis.split('Sentence ')
        for sentence_block in sentences[1:]: # Skip the first empty element
            lines = sentence_block.split('\n')
            if len(lines) >= 4:
                sentence_text = lines[0].split(': ', 1)[1].strip().replace('"', '')
                sarcasm_detected = lines[1].split(': ', 1)[1].strip()
                confidence_level = lines[2].split(': ', 1)[1].strip()
                explanation = lines[3].split(': ', 1)[1].strip() if len(lines) > 3 else "No explanation provided"
                sentence_analyses.append({
                    'sentence': sentence_text,
                    'sarcasm': sarcasm_detected,
                    'confidence': confidence_level,
                    'explanation': explanation
                })
        return sentence_analyses
    return [{"error": "Could not get response from AI."}]

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/check_sarcasm', methods=['POST'])
def check_sarcasm():
    text = request.form['text']
    analysis = get_sarcasm_analysis(text)
    return render_template('result.html', text=text, analysis=analysis, original_text=text)

if __name__ == '__main__':
    app.run(debug=True)
