FROM python:3.11-slim as builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src-bot/ .

FROM gcr.io/distroless/python3

COPY --from=builder /usr/local /usr/local
COPY --from=builder /app /app

WORKDIR /app

ENV PYTHONPATH=/usr/local/lib/python3.11/site-packages

CMD ["bot.py"]
