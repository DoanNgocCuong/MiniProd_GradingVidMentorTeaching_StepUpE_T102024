### 4.1. Cài đặt Dependencies
```bash
# Cài đặt các dependencies trong package.json
npm install

# Cài đặt Tailwind CSS và các tools liên quan
npm install -D tailwindcss@latest postcss@latest autoprefixer@latest
```

### 4.2. Khởi chạy Development Server
```bash
npm start
```
Ứng dụng sẽ chạy tại http://localhost:3000

### 4.3. Build Production
```bash
npm run build
```

## 5. Lưu ý quan trọng
1. Đảm bảo Node.js đã được cài đặt trên máy
2. Chạy các lệnh npm từ thư mục gốc của project (ui_react)
3. Kiểm tra file package.json có đầy đủ dependencies cần thiết
4. Cài đặt lại node_modules nếu gặp lỗi: `npm install`
5. Đảm bảo các file cấu hình (postcss.config.js, tailwind.config.js) ở đúng vị trí

## 6. Troubleshooting phổ biến
1. Lỗi "Module not found": Chạy `npm install`
2. Lỗi về Tailwind: Kiểm tra các file cấu hình và cài đặt lại
3. Lỗi khi chạy npm start: Kiểm tra package.json và cài đặt react-scripts