from TTS.api import TTS
import os
from datetime import datetime


device = "cpu"

# Init TTS
# tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)
tts = TTS(model_path="tts_models--multilingual--multi-dataset--xtts_v2", config_path="tts_models--multilingual--multi-dataset--xtts_v2/config.json", progress_bar=False, gpu=False)

base_file_name = "voice_hg.wav"
base_file_path = os.path.join("static", "voice_datas", base_file_name)

def define_text_to_speech(text: str) -> str:
    print("TTS start")
    result_file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    result_file_path = os.path.join("static", "temp", result_file_name)
    print("result_file_path =", result_file_path)
    tts.tts_to_file(text=text, 
                file_path=result_file_path, 
                speaker_wav=base_file_path, 
                language="ko")
    print("TTS finish")
    return result_file_name

if __name__ == "__main__":
    define_text_to_speech("안녕")