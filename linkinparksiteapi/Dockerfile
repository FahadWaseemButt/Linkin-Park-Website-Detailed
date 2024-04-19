# Use the official Python 3.11 image as the base
FROM python:3.11

# Set the working directory in the container
WORKDIR /linkinparksiteapi

# Copy the requirements.txt file to the working directory
COPY requirements.txt .

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . .

# Expose the port on which your Flask app is running
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "server.py"]