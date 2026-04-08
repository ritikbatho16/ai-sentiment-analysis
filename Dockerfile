# Base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flask textblob

# Download TextBlob corpora
RUN python -m textblob.download_corpora lite

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]