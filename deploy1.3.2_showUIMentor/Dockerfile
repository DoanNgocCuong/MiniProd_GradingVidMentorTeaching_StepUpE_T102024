# Sử dụng hình ảnh Node.js chính thức từ Docker Hub
FROM node:14

# Tạo thư mục làm việc trong container
WORKDIR /app

# Sao chép file package.json và package-lock.json vào container
COPY package*.json ./

# Cài đặt các dependencies
RUN npm install

# Sao chép tất cả các tệp còn lại vào container
COPY . .

# Mở cổng ứng dụng
EXPOSE 3000

# Lệnh để chạy ứng dụng
CMD ["npm", "start"]