# Use official Node.js image from Docker Hub
FROM node:14

# Set working directory in container
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy all remaining files
COPY . .

# Expose application port
EXPOSE 5000

# Command to run the application
CMD ["npm", "start"]