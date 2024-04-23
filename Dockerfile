FROM python:3.10-slim

WORKDIR /workspace
    
COPY . .

RUN pip install torch==2.2.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
