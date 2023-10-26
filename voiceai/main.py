import io
import os

from fastapi import FastAPI, UploadFile, HTTPException
from pydantic import BaseModel
import uuid

import whisper

model = whisper.load_model("base")

app = FastAPI()


class SpeechToTextResponse(BaseModel):
    text: str


@app.post("/speech-to-text/", response_model=SpeechToTextResponse)
async def speech_to_text(file: UploadFile):
    # Check if the file is a valid wav file
    tmp_filename = f"tmp/{uuid.uuid4()}_{file.filename}"
    with open(tmp_filename, 'wb') as f:
        f.write(await file.read())

    result = model.transcribe(tmp_filename)
    os.remove(tmp_filename)

    return SpeechToTextResponse(text=result['text'].strip())
