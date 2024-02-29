# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the files into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install -r requirements.txt

COPY push_aws.py .

# Set the command to run the application
CMD ["python", "push_aws.py"]


