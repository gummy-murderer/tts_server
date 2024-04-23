from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from melo.api import TTS
from datetime import datetime
import os

from lib.preprcessing import preprocess_text
from lib.const import LANGUAGE, SPEAKER

app = FastAPI()

model = TTS(language=LANGUAGE, 
            device='cpu',
            # config_path="./MeloTTS_kr/config.json"
            )
speaker_ids = model.hps.data.spk2id

os.makedirs(os.path.join("static", "temp"), exist_ok=True)


class SynthesizeRequest(BaseModel):
    text: str
    speed: float = 1.0

@app.post("/tts")
def convert_text_to_speech(request: SynthesizeRequest):
    # try:
    preprocessed_text = preprocess_text(request.text)

    output_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
    output_path = os.path.join("static", "temp", output_name)

    model.tts_to_file(preprocessed_text, speaker_ids[SPEAKER], output_path, speed=request.speed)

    return {"message": "Text converted to speech", "output_path": output_path}
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))