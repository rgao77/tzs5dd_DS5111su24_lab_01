FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "pytest"]

