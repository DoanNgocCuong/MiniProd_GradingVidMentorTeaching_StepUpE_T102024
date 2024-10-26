// app.js
const express = require('express');
const app = express();
const openAIRoutes = require('./routes/openAIRoutes');
require('dotenv').config();  // Đọc các biến môi trường từ tệp .env

// Middleware
app.use(express.json());  // Để đọc dữ liệu JSON từ body của request

// Đăng ký các routes
app.use('/api', openAIRoutes);

// Thiết lập cổng cho server
const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server đang chạy trên cổng ${PORT}`);
});
