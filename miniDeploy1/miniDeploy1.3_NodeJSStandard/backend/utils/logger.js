// Import thư viện winston để ghi log
const winston = require('winston');

// Tạo một logger mới với cấu hình cụ thể
const logger = winston.createLogger({
  // Mức độ log là 'info' (thông tin)
  level: 'info',
  // Định dạng log là JSON
  format: winston.format.json(),
  // Thêm thông tin về dịch vụ (service) vào log
  defaultMeta: { service: 'openai-service' },
  // Thiết lập nơi lưu trữ log, ở đây là console (màn hình)
  transports: [
    new winston.transports.Console()
  ]
});

// Xuất khẩu logger để sử dụng ở các file khác
module.exports = logger;
