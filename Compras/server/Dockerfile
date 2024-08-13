# Use the official Node.js image
FROM node:20-alpine

# Set the working directory
WORKDIR /app/server

# Copy the application code and package.json into the container
COPY src/ /app/server/src/
COPY package.json /app/server/

# Install the required Node.js packages
RUN npm install

# Copy the start script file and make it executable
COPY scripts/script.sh /app/server/scripts/
RUN chmod +x /app/server/scripts/script.sh

# # Define the entry point
ENTRYPOINT ["/app/server/scripts/script.sh"]
