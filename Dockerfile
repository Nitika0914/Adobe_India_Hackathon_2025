FROM --platform=linux/amd64 python:3.10-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the app code
COPY app/ ./app/

# Create mount points for input/output (optional safety)
VOLUME ["/app/input", "/app/output"]

# Run main.py
CMD ["python", "app/main.py"]
