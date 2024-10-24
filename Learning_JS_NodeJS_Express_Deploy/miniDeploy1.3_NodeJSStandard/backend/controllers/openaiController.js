// Import dịch vụ openaiService
const openaiService = require('../services/openaiService');

// Hàm để xử lý prompt từ người dùng
const processPrompt = async (req, res) => {
  try {
    // Lấy systemPrompt và userInputPrompt từ yêu cầu POST
    const { systemPrompt, userInputPrompt } = req.body;
    // Gọi hàm getOpenAIResponse để lấy phản hồi từ OpenAI
    const response = await openaiService.getOpenAIResponse(systemPrompt, userInputPrompt);
    // Gửi phản hồi lại cho người dùng dưới dạng JSON
    res.json({ response });
  } catch (error) {
    // Nếu có lỗi, gửi mã lỗi 500 và thông báo lỗi
    res.status(500).json({ error: error.message });
  }
};

// Xuất khẩu hàm processPrompt để sử dụng trong routes
module.exports = {
  processPrompt
};
