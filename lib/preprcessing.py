import re
import json


def preprocess_text(text):
    text = re.sub(r'[^\w\s]', '', text)

    text = re.sub(r'\s+', ' ', text)

    text = text.strip()
    
    return text