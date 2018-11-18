# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Abrir puerto 80
EXPOSE 80

# Variables
ARG buildtime_variable=default_value

# Define environment variables
ENV REDIS_URL=$buildtime_variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
