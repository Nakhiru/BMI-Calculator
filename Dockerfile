FROM python:3.11-slim

WORKDIR /app

COPY bmi_calculator.py .

COPY test_bmi_calculator.py .

ENTRYPOINT ["python", "bmi_calculator.py"]