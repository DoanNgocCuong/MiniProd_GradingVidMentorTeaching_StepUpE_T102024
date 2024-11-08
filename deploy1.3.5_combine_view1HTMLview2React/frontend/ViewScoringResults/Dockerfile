# Sử dụng Node.js image chính thức từ Docker Hub
FROM node:18-alpine AS build

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Sao chép file package.json và package-lock.json
COPY package*.json ./

# Cài đặt các dependencies
RUN npm install

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Build ứng dụng cho production
RUN npm run build

# Sử dụng Nginx để phục vụ ứng dụng
FROM nginx:stable-alpine

# Sao chép file build từ stage trước vào thư mục mặc định của Nginx
COPY --from=build /app/build /usr/share/nginx/html

# Sao chép cấu hình Nginx nếu cần (tùy chọn)
# COPY nginx.conf /etc/nginx/nginx.conf

# Expose cổng mà Nginx sẽ lắng nghe
EXPOSE 80

# Khởi động Nginx
CMD ["nginx", "-g", "daemon off;"]
