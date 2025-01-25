from dotenv import load_dotenv
import google.generativeai as genai
import os
import re
from text import test_response 
from sarcasm_sentence import sarc_sentence
from sarcasm_paragraph import sarc_paragraph

load_dotenv()
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY environment variable set. Please set it before running the app.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')
#response = model.generate_content(prompt)

sarc_paragraph_instance = sarc_paragraph(test_response, sentences_arr=[])

for sentence in sarc_paragraph_instance.sentences_arr:
    print(sentence)
    print()

def paragraph_to_array(input_paragraph):
    paragraph_arr = []
    for sentence in input_paragraph.split("."):
        paragraph_arr.append((sentence, 0))
    return paragraph_arr

    

   
       







