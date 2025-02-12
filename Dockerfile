FROM python:3.9-slim

WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code and model files
COPY app.py .
COPY scaler.pkl .
COPY regressor.pkl .

# Expose the port Gradio will run on
EXPOSE 7860

# Start the application
CMD ["python", "app.py"] 