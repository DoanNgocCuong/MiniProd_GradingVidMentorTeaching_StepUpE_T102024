### HowRunDeploy2.md

- Chú ý quan trọng:việc test riêng frontend này, nếu muốn backend bật lên thì phải run backend riêng. 

#### 0. Click Go Live
- Truy cập ứng dụng tại `http://localhost:3000`. 
hoặc http://127.0.0.1:5502/frontend/index.html hoặc địa chỉ IP của laptop


#### 1. Run `server.js`
- Chạy server Node.js bằng lệnh:
  ```bash
  node server.js
  ```
- Truy cập ứng dụng tại `http://localhost:3000`. hoặc địa chỉ IP của laptop 

#### 2. Run NPM
- Khởi động ứng dụng với NPM:
```bash
npm install
```

```bash
npm start
```
- Truy cập ứng dụng tại `http://localhost:3000`. hoặc 

#### 3. Run NPM with Docker
- Xây dựng và chạy ứng dụng trong Docker:
  ```bash
  docker build -t your-app-name .
  docker run -p 5000:5000 your-app-name
  ```
- Truy cập ứng dụng tại `http://localhost:3000`. 
- (bạn vẫn cần bật backend riêng để test cái này)
Hoặc đến đây đóng cái docker-compose run 1 cái test luôn cả backend, frontend



Dưới đây là bảng đã bỏ cột ghi chú, chỉ hiển thị các URL cho các môi trường:

| **Môi trường**                               | **Frontend URL**                                                                                           | **Backend URL**                                                                                |
|----------------------------------------------|------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| **1. Backend (Local & Docker)**              | -                                                                                                          | `http://localhost:3000` <br> `http://10.17.46.238:3000` <br> `http://localhost:25035`          |
| **2. Frontend (Go Live & Docker)**           | `http://127.0.0.1:5502/frontend/index.html` <br> `http://10.17.46.238:5502/frontend/index.html` <br> `http://localhost:25036` | -                                                                                              |
| **3. Cả backend và frontend (Go Live)**      | `http://127.0.0.1:5502/frontend/UIBuilder/index.html` <br> `http://10.17.46.238:5502/frontend/UIBuilder/index.html` | `http://localhost:3000` <br> `http://10.17.46.238:3000`                                        |
| **4. Full Docker (Local & IP)**              | `http://localhost:25036` <br> `http://10.17.46.238:25036`                                                 | `http://localhost:25035` <br> `http://10.17.46.238:25035`                                      |
| **5. Triển khai trên Server**                | `http://103.253.20.13:25036`                                                                              | `http://103.253.20.13:25035`                                                                    |

---
