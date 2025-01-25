class sarc_sentence:
    def __init__(self, text, sarc, sarc_percent, explanation):
        self.text = text
        self.sarc = sarc
        self.sarc_percent = sarc_percent
        self.explanation = explanation

    def __str__(self):
        return f"Text: {self.text}\n Sarcasm Detected: {self.sarc}\n Confidence Level: {self.sarc_percent}%\n Explanation: {self.explanation}\n"

    @staticmethod
    def parse_sarc_sentence(sarc_tuple):
        text, sarc, sarc_percent, explanation = sarc_tuple
        return sarc_sentence(text, sarc, int(sarc_percent), explanation)