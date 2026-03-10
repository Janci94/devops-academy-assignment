# Use a lightweight Alpine-based image to save space
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy only dependency files to leverage Docker layer caching
# This prevents re-running npm install if dependencies didn't change
COPY package*.json ./

# Install dependencies and clean npm cache in the same layer to keep it small
RUN npm install --production && npm cache clean --force

# Copy the rest of the application files
COPY . .

# Use a non-root user for better security
USER node

# Define the command to run the app
CMD ["node", "index.js"]