### HowRunDeploy2.md

#### 0. Click Go Live
- Truy cập ứng dụng tại `http://localhost:3000`.

#### 1. Run `server.js`
- Chạy server Node.js bằng lệnh:
  ```bash
  node server.js
  ```
- Truy cập ứng dụng tại `http://localhost:3000`.

#### 2. Run NPM
- Khởi động ứng dụng với NPM:
```bash
npm install
```

```bash
npm start
```
- Truy cập ứng dụng tại `http://localhost:3000`.

#### 3. Run NPM with Docker
- Xây dựng và chạy ứng dụng trong Docker:
  ```bash
  docker build -t your-app-name .
  docker run -p 3000:3000 your-app-name
  ```
- Truy cập ứng dụng tại `http://localhost:3000`.



=======================



Run docker: 
1.
```bash
docker-compose up --build
```