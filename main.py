from fastapi import FastAPI
from fastapi.responses import FileResponse

from melo_my.api import TTS
import os
import gc

from lib.preprcessing import preprocess_text, make_output_path
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
def convert_text_to_speech(contents: str):
    try:
        result = None
        output_path = make_output_path()
        result = model.tts_to_file(preprocess_text(contents), speaker_ids[KR["speaker"]], output_path)
        return FileResponse(output_path)
    except Exception as e:
        return {"error": str(e)}
    finally:
        del result
        gc.collect()