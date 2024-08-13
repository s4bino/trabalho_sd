# Use the official Ubuntu base image
FROM ubuntu:latest

# Install Python, pip, curl, and other necessary packages
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv curl

# Create a virtual environment in /opt/venv
RUN python3 -m venv /opt/venv

# Set the virtual environment path
ENV PATH="/opt/venv/bin:$PATH"

# Set the working directory
WORKDIR /app/scrapping

# Copy the application code and requirements.txt into the container
COPY /src /app/scrapping/
COPY requirements.txt /app/scrapping/

# Install the required Python packages
RUN pip install --no-cache-dir -r /app/scrapping/requirements.txt

# Copy the script.sh file and make it executable
COPY scripts/script.sh /app/scrapping/scripts/
RUN chmod +x /app/scrapping/scripts/script.sh

# Define the entry point
ENTRYPOINT ["/app/scrapping/scripts/script.sh"]