- 
```bash
npm install axios dotenv express cors <if don't have a package.json> / npm install <>
```
- Run 2 node:
```bash
node backend/backend_app.js
node connect_app.js
```

CHÚ Ý QUAN TRỌNG: File .env PHẢI ĐẶT CÙNG CẤP VỚI NƠI RUN. Nếu run: 
```node backend/backend_app.js``` thì file .env phải đặt cùng cấp với nơi 2 thư mục backend, fronntend, connect_app.js
```node connect_app.js``` thì file .env phải đặt trong thư mục backend