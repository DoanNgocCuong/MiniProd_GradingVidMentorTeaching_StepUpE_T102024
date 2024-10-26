// Import express để tạo ứng dụng web
const express = require('express');
// Import path để làm việc với đường dẫn file
const path = require('path');
// Tạo một ứng dụng Express mới
const app = express();
// Import các route từ openaiRoutes
const openaiRoutes = require('./routes/openaiRoutes');
// Import middleware xử lý lỗi
const errorHandler = require('./middlewares/errorHandler');

// Sử dụng middleware để phân tích cú pháp JSON
app.use(express.json());
// Sử dụng middleware để phân tích dữ liệu từ URL
app.use(express.urlencoded({ extended: true }));

// Thiết lập thư mục tĩnh để phục vụ các file frontend
app.use(express.static(path.join(__dirname, '../frontend')));

// Sử dụng các route từ openaiRoutes cho đường dẫn '/api'
app.use('/api', openaiRoutes);

// Sử dụng middleware xử lý lỗi
app.use(errorHandler);

// Xuất khẩu ứng dụng để sử dụng trong server.js
module.exports = app;
