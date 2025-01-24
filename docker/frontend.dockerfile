# Use the official Node.js image as the base image
FROM node:18

# Update and install necessary tools
RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY src src/

# Set the working directory
WORKDIR /src/frontend/chromify_frontend

# Install dependencies
RUN npm install
RUN npm install js-base64 axios

# Expose the port the app runs on
EXPOSE 5137

# Start the application
CMD ["npm", "run", "dev"]
