# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the files into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install libgl1 libglib2.0-0 -y
RUN pip install gitpython setuptools

COPY animal_detect.py .

# Set the command to run the application
CMD ["python", "animal_detect.py"]
