from pathlib import Path
import os

# LANGUAGE = "KR"
# LANGUAGE = "EN"
# SPEAKER = "EN-US"

EN = {"language": "EN", "speaker": "EN-US"}
KR = {"language": "KR", "speaker": "KR", "path":"resources/MeloTTS_kr"}

# KR_MODEL_PATH = Path(__file__).parent.parent / 'resources'/ 'bert-kor-base'
KR_MODEL_PATH = os.path.join(os.getcwd(), "resources", "bert-kor-base")