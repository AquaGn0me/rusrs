test_text = "I love coming to the office. I love how there is no natural light, and only 1 bathroom for 500 people." 

prompt= f""""

    You are an advanced AI trained to analyze text for sarcasm. Your task is to evaluate 
    an entire block of text, identify any portions that might be sarcastic, and analyze them. 
    Maintain consistency, coherence, and accuracy in your analysis. The same input should elicit the same output every time.
    If there is not enough context to make an accurate determination, for example if only a single word is inputted, reply with:
    **UNSURE**

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
    *"[Potential sarcastic part]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage]
    Explanation: [Analysis of why this part may or may not be sarcastic.]
    *"[Next potential sarcastic part]"
    Sarcasm Detected: [Yes/No]
    Confidence Level: [Percentage]
    Explanation: [Analysis of why this part may or may not be sarcastic.]
    If no sarcasm is detected, state clearly: "No sarcasm detected in the block of text."

    Here is the text: {test_text}

    Review your analysis of the block of text for coherence and depth. 
    Ensure you have thoroughly examined all portions of the text for possible 
    sarcasm and that your justifications reference specific elements like tone, 
    word choice, punctuation, or context.

    If there is ambiguity in whether a part is sarcastic, explain both sides 
    of the interpretation and adjust the confidence level to reflect the uncertainty.
    Double-check that all sarcastic elements have been identified and that the analysis 
    aligns with typical patterns of sarcasm in human communication.
    """

test_response = """Detected Sarcastic Parts:
* "I love coming to the office"
Sarcasm Detected: Yes
Confidence Level: 80%
Explanation: This statement is sarcastic because it conveys an opposite sentiment than the literal meaning. The office environment is not typically perceived as positive, and the speaker's use of "love" is exaggerated and incongruous to the context, revealing a mocking tone.

* "I love how there is no natural light"
Sarcasm Detected: Yes
Confidence Level: 90%
Explanation: This statement is sarcastic because it emphasizes the lack of a feature (natural light) that is generally considered desirable in office settings. The hyperbole ("no natural light") and the ironic appreciation ("I love how") highlight the speaker's frustration with the working conditions.

* "and only 1 bathroom for 500 people"
Sarcasm Detected: Yes
Confidence Level: 70%
Explanation: This statement is likely sarcastic as it draws attention to an extreme disparity between the number of employees and the availability of restrooms. The use of the specific number "500" and the contrast with "only 1" bathroom suggests an exaggeration that is intended to convey criticism or frustration."""