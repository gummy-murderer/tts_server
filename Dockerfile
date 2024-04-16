FROM python:3.10

WORKDIR /workspace

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential gcc g++ make && \
    rm -rf /var/lib/apt/lists/*
    
COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
