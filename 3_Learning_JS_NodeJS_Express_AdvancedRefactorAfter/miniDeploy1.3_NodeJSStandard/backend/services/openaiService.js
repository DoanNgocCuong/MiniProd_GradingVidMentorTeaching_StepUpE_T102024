// Import thư viện axios để gửi yêu cầu HTTP
const axios = require('axios');
// Import cấu hình từ file config.js
const config = require('../config/config');
// Import logger để ghi log
const logger = require('../utils/logger');

// Hàm để lấy phản hồi từ OpenAI
const getOpenAIResponse = async (systemPrompt, userInputPrompt) => {
  // Kiểm tra nếu systemPrompt hoặc userInputPrompt bị trống
  if (!systemPrompt || !userInputPrompt) {
    throw new Error('System prompt và user input prompt không được để trống.');
  }

  // URL của OpenAI API
  const url = 'https://api.openai.com/v1/chat/completions';

  // Tạo payload (dữ liệu) để gửi đến API
  const payload = {
    model: 'gpt-3.5-turbo', // Có thể thay đổi thành 'gpt-4' nếu bạn có quyền truy cập
    messages: [
      { role: 'system', content: systemPrompt }, // Thông điệp từ hệ thống
      { role: 'user', content: userInputPrompt } // Thông điệp từ người dùng
    ]
  };

  try {
    // Gửi yêu cầu POST đến OpenAI API
    const response = await axios.post(url, payload, {
      headers: {
        // Thêm API key vào header để xác thực
        'Authorization': `Bearer ${config.openaiApiKey}`,
        // Đặt loại nội dung là JSON
        'Content-Type': 'application/json'
      }
    });

    // Lấy kết quả từ phản hồi của API
    const result = response.data.choices[0].message.content.trim();
    // Ghi log kết quả
    logger.info('Phản hồi từ OpenAI: ' + result);
    // Trả về kết quả
    return result;

  } catch (error) {
    // Nếu có lỗi, ghi log lỗi
    logger.error('Lỗi trong quá trình gọi API: ' + error.toString());
    // Ném lỗi để xử lý ở nơi khác
    throw error;
  }
};

// Xuất khẩu hàm getOpenAIResponse để sử dụng ở file khác
module.exports = {
  getOpenAIResponse
};
