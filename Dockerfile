
FROM python:3.11-slim

WORKDIR /app

COPY data.csv .
COPY check_data.py .

RUN pip install --no-cache-dir pandas

CMD ["python", "check_data.py"]
