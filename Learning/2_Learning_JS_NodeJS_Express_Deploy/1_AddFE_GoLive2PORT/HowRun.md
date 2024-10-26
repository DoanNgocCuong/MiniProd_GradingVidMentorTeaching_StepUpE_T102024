1. BACKEND gồm các API Endpoint. => Khởi động Backend. 
```bash

npm install axios dotenv express cors <khi chưa có file package.json khi bạn chạy lệnh này nó sẽ tạo> / npm install  <if have file package.json>
node app.js / npm start
```

2. FRONTEND: Build 1 frontend đơn giản với 1 file HTML và 1 file JS. 
- File JS sử dụng Fetch API để gọi API Endpoint của Backend. 

3. CHÚ Ý QUAN TRỌNG: File .env PHẢI ĐẶT CÙNG CẤP VỚI NƠI RUN. Nếu run: 
```node backend/backend_app.js``` thì file .env phải đặt cùng cấp với nơi 2 thư mục backend, fronntend, connect_app.js
```node connect_app.js``` thì file .env phải đặt trong thư mục backend





### Có Vấn đề gì với cách làm này không? 
- Tuy là API Endpoint Backend không làm lộ API Key của OpenAI nhưng mà người dùng vẫn có thể sử dụng API Endpoint Backend của mình mà, đúng chứ? 

Trả lời: 
- Đúng, người dùng có thể gửi yêu cầu đến API Endpoint của bạn. Tuy nhiên, bạn có thể áp dụng một số biện pháp bảo mật để hạn chế việc sử dụng không mong muốn, chẳng hạn như:
  - **Xác thực**: Thêm cơ chế xác thực (như token) để chỉ cho phép người dùng đã đăng nhập hoặc có quyền truy cập.
  - **Giới hạn tần suất**: Sử dụng middleware để giới hạn số lượng yêu cầu mà một người dùng có thể gửi trong một khoảng thời gian nhất định.
  - **Kiểm tra dữ liệu đầu vào**: Đảm bảo rằng dữ liệu đầu vào từ người dùng được kiểm tra và xác thực để tránh các cuộc tấn công như SQL Injection hoặc XSS.
  - **Ghi log**: Theo dõi và ghi lại các yêu cầu đến API để phát hiện các hành vi bất thường.