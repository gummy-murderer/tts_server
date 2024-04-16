from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
import os

# from tts import define_text_to_speech

app = FastAPI()


class Item(BaseModel):
    contents: str

@app.post("/v1/api/tts")
def read_item(item: Item):
    # result_file_name = define_text_to_speech(item.contents)
    result_file_name = "20240416_192029.wav"
    return {"file_name": result_file_name}

@app.get("/v1/api/tts_get/{file_name}")
def read_item(file_name: str):
    result_file_path = os.path.join("static", "temp", file_name)
    return FileResponse(result_file_path)