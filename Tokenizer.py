import re 

def analyze(voice_data):
    loweredSentence = voice_data.lower()
    wordList = list(filter(None,re.split('[.,!?]', loweredSentence)))
    return wordList