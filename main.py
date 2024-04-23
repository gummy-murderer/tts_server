from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from melo.api import TTS
from datetime import datetime
import os

from lib.preprcessing import preprocess_text
from lib.const import KR

app = FastAPI()

model = TTS(language=KR["language"], 
            device='cpu',
            config_path=os.path.join(KR["path"], "config.json"),
            ckpt_path=os.path.join(KR["path"], "checkpoint.pth")
            )
speaker_ids = model.hps.data.spk2id

os.makedirs(os.path.join("static", "temp"), exist_ok=True)


@app.get("/api/v1/tts")
def convert_text_to_speech(contents: str, file_return: bool):
    try:
        preprocessed_text = preprocess_text(contents)

        output_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".wav"
        output_path = os.path.join("static", "temp", output_name)

        result = model.tts_to_file(preprocessed_text, speaker_ids[KR["speaker"]], output_path)

        if file_return:
            return FileResponse(output_path)
        return {"message": "Text converted to speech", "output_path": output_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))