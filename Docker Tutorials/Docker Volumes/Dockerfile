FROM python:3.11-slim

# Set the working directory in the container (Also create it)
WORKDIR /app

# Create the directory for logs
RUN mkdir logs

# Copy the current directory contents into the container at /app
COPY . /app

# Command to run on container start
CMD ["python", "run.py"]
