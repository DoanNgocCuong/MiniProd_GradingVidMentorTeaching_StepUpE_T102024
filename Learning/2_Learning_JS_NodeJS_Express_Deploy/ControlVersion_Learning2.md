## 0_Only_1file_JS_to_API
Đóng gói 1 file JS thành 1 API Endpoint. 
Tuy nhiên API Endpoint này chỉ có 1 hàm duy nhất là OpenAI với method POST. 

Với bài toán thực tế 1 Backend sẽ có rất nhiều hàm, mỗi hàm sẽ là 1 API Endpoint, ....

```bash
npm install axios dotenv / npm install <if have package.json>
node openai_test.js / npm start <if have package.json>
```

## 1_Add_FE_GoLive
- cd vào `backend` để khởi động Backend tại 3001
```bash
npm install axios dotenv cors / npm install <if have package.json>
node backend-api.js / npm start <if have package.json>
```

- Frontend được đóng gói trong 1 file HTML và 1 file JS. (File JS sử dụng Fetch API để gọi API Endpoint của Backend). 
- Frontend ấn Go Live -> mặc định được khởi động tại: http://localhost:5500/index.html



