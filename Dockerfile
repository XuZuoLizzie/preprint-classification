# Use an official Python runtime as a parent image
FROM python:3.8-slim-bullseye

# Set the working directory in the container
# WORKDIR /usr/src/app
WORKDIR /code

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Download the SciSpaCy large model
RUN pip install https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.5.0/en_core_sci_lg-0.5.0.tar.gz

# Run the script when the container launches
CMD ["python", "classification_model.py"]