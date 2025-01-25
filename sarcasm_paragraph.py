import re
from sarcasm_sentence import sarc_sentence  # Ensure sarc_sentence is imported

class sarc_paragraph:
    def __init__(self, text, sentences_arr=None):
        self.text = text
        self.sentences_arr = sentences_arr if sentences_arr is not None else []
        self.parse_text()

    def parse_text(self):
        # Parse text into array of sarc_sentence objects
        pattern = re.compile(r'\* "(.*?)"\nSarcasm Detected: (Yes|No)\nConfidence Level: (\d+)%\nExplanation: (.*?)\n\n', re.DOTALL)
        matches = pattern.findall(self.text)
        for match in matches:
            sentence = sarc_sentence.parse_sarc_sentence(match)
            self.sentences_arr.append(sentence)

    def __str__(self):
        return f"{self.text}"