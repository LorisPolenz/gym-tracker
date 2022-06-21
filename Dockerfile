FROM python:3.9-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY fetch.py .

RUN mkdir ./gym-data

CMD ["python", "./fetch.py"]