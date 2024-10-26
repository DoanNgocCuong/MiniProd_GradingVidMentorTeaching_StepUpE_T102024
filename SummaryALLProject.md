## 1. Cấu trúc project

```bash
backend/  # Thư mục chứa mã nguồn backend
├── config/  # Thư mục cấu hình
│   ├── config.js  # Tệp cấu hình chung của ứng dụng
│   └── database.js  # Tệp cấu hình kết nối cơ sở dữ liệu
├── controllers/  # Thư mục chứa các controller (điều khiển)
│   └── openaiController.js  # Controller xử lý logic cho OpenAI API
├── models/  # Thư mục chứa các mô hình dữ liệu
│   └── openaiModel.js  # Mô hình dữ liệu cho OpenAI
├── routes/  # Thư mục chứa các định tuyến
│   └── openaiRoutes.js  # Định tuyến cho các endpoint của OpenAI API
├── services/  # Thư mục chứa các service (dịch vụ)
│   └── openaiService.js  # Service tương tác với OpenAI API
├── middleware/  # Thư mục chứa các middleware
│   ├── authMiddleware.js  # Middleware xử lý xác thực người dùng
│   └── errorHandler.js  # Middleware xử lý lỗi toàn cục
├── utils/  # Thư mục chứa các tiện ích chung
│   ├── helperFunctions.js  # Các hàm trợ giúp và tiện ích
│   └── logger.js  # Hàm ghi log cho ứng dụng
├── app.js  # Tệp khởi tạo ứng dụng và cấu hình middleware
└── server.js  # Tệp khởi động server và lắng nghe kết nối

frontend/  # Thư mục chứa mã nguồn frontend
├── assets/  # Thư mục chứa tài nguyên tĩnh
│   ├── css/  # Thư mục chứa file CSS
│   │   └── style.css  # Tệp CSS chính cho giao diện
│   ├── js/  # Thư mục chứa file JavaScript
│   │   ├── api/  # Thư mục chứa các file tương tác với API
│   │   │   └── openaiApi.js  # Tệp JavaScript gọi OpenAI API từ frontend
│   │   ├── utils/  # Thư mục chứa các hàm tiện ích
│   │   │   └── validators.js  # Các hàm kiểm tra và xác thực dữ liệu
│   │   └── app.js  # Tệp JavaScript chính cho ứng dụng frontend
├── images/  # Thư mục chứa hình ảnh
│   └── logo.png  # Logo hoặc hình ảnh sử dụng trong ứng dụng
└── index.html  # Tệp HTML chính của ứng dụng frontend
```
- File `server.js`: có thể được cấu hình để khởi động server và phục vụ các file tĩnh như .html, .css, .js, thay thế cho việc sử dụng Go Live. `server.js` chịu trách nhiệm khởi động server và lắng nghe các yêu cầu, nhưng không trực tiếp giao tiếp với frontend. Thay vào đó, các route và controller mới là thành phần xử lý yêu cầu từ frontend và trả về kết quả.
- Khi frontend gửi một yêu cầu API (HTTP request) đến backend, yêu cầu sẽ được định tuyến qua `openaiRoutes.js`, điều hướng đến `openaiController.js` để xử lý logic nghiệp vụ (có thể gọi đến `openaiService.js` để lấy dữ liệu từ OpenAI API), sau đó controller trả lại kết quả cho frontend.


## 2. HowRunDeploy.md

0. Click Go Live
- Truy cập ứng dụng tại `http://localhost:3000`.

1. Run `server.js`
- Chạy server Node.js bằng lệnh:
  ```bash
  node server.js
  ```
- Truy cập ứng dụng tại `http://localhost:3000`.

2. Run NPM
- Khởi động ứng dụng với NPM:
```bash
npm install
```

```bash
npm start
```
- Truy cập ứng dụng tại `http://localhost:3000`.

3. Run NPM with Docker
- Xây dựng và chạy ứng dụng trong Docker:
  ```bash
  docker build -t your-app-name .
  docker run -p 3000:3000 your-app-name
  ```
- Truy cập ứng dụng tại `http://localhost:3000`.