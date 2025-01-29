# Use the official Python image from Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY api/requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code into the container
COPY api/ /app/

# Expose port 8000 for Django
EXPOSE 8000

# Set the default command to run Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
