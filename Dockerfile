# Use the official Python image
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

# Installing required packages
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy the local code to the container
COPY ./app /app/app

