# Use official Python image from Docker Hub
FROM python:3.9

# Set working directory in container
WORKDIR /app

# Copy requirements file
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all remaining files
COPY . .

# Expose application port
EXPOSE 3000

# Command to run the application
CMD ["python", "api_database3apiGhiDe.py"]
