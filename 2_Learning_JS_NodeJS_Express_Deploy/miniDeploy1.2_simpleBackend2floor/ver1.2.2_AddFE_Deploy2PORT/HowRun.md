Vô Backend, run Frontend bằng cách click vào Go Live 
```bash

npm install axios dotenv express cors <khi chưa có file package.json khi bạn chạy lệnh này nó sẽ tạo> / npm install  <if have file package.json>
node app.js / npm start
```

- `node backend_APIBackend_app.js`: Chạy trực tiếp từ file `app.js`.
- `npm start`: Chạy ứng dụng thông qua lệnh được định nghĩa trong file `package.json`.

CHÚ Ý QUAN TRỌNG: File .env PHẢI ĐẶT CÙNG CẤP VỚI NƠI RUN. Nếu run: 
```node backend/backend_app.js``` thì file .env phải đặt cùng cấp với nơi 2 thư mục backend, fronntend, connect_app.js
```node connect_app.js``` thì file .env phải đặt trong thư mục backend