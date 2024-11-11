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

# Đảm bảo các file có quyền thực thi
RUN chmod +x /app/server.js

# Expose application port
EXPOSE 5000

# Sử dụng nodemon để auto-reload trong development
CMD ["node", "server.js"]