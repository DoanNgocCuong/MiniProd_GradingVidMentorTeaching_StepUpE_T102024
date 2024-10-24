
// Import thư viện dotenv để đọc các biến môi trường từ file .env
const dotenv = require('dotenv');

// Gọi hàm config() để thiết lập các biến môi trường
dotenv.config();

// Xuất khẩu (export) các cấu hình để các file khác có thể sử dụng
module.exports = {
  // Lấy API key của OpenAI từ biến môi trường
  openaiApiKey: process.env.OPENAI_API_KEY,
  // Thiết lập cổng (port) cho ứng dụng, mặc định là 3000 nếu không có
  port: process.env.PORT || 3000
};
