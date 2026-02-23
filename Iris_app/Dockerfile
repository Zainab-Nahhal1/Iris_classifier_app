# Use the official Python image from the Docker Hub
FROM python:3.13

# Set the working directory in the container
WORKDIR /app

# Set Hugging Face cache directory
ENV TRANSFORMERS_CACHE=/app/model_cache

# Copy the requirements file into the container
COPY /requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download the model during build (not at runtime)
RUN python -c "from transformers import pipeline; pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')"

# Copy the rest of the application code into the container (excluding .env for security)
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]