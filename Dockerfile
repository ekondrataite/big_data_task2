FROM python:3.12-slim

# Working directory in the container
WORKDIR /regression_model

# Copy all files into the directory
COPY . /regression_model

# Read requirements
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "main.py"]
