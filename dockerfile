FROM python:latest

WORKDIR /app

COPY mark.py .

CMD ["python", "mark.py"]