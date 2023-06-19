# Use an official Python runtime as a parent image
FROM python:3.8.10

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run producer.py when the container launches
CMD ["python", "producer.py"]
