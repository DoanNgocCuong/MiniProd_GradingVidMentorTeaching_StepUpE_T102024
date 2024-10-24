// Import logger để ghi log lỗi
const logger = require('../utils/logger');

// Hàm middleware để xử lý lỗi
const errorHandler = (err, req, res, next) => {
  // Ghi log stack trace của lỗi
  logger.error(err.stack);
  // Gửi mã lỗi 500 và thông báo lỗi chung
  res.status(500).json({ error: 'Đã xảy ra lỗi trong hệ thống!' });
};

// Xuất khẩu middleware để sử dụng trong app.js
module.exports = errorHandler;
