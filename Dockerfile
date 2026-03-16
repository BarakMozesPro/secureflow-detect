FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install pcapy-ng
EXPOSE 8338
CMD ["python", "sensor.py"]
