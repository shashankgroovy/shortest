FROM python:3.11-alpine

WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt requirements.txt
RUN pip install -r ./requirements.txt

# Copy the api folder
COPY . .

# Expose the api port
EXPOSE 8000

# Indicate the initializing command
# NOTE: the number of workers is kept at 1, since we are storing all urls in-memory, and will run into memory miss if workers are increased
# To work with more workers, introduce Redis as shared cache resource.
CMD ["gunicorn", "shortest.app:bootload()", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]


