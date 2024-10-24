// Import express để tạo router
const express = require('express');
// Tạo một router mới
const router = express.Router();
// Import openaiController để xử lý logic
const openaiController = require('../controllers/openaiController');

// Khi nhận yêu cầu POST tới '/process-prompt', gọi hàm processPrompt
router.post('/process-prompt', openaiController.processPrompt);

// Xuất khẩu router để sử dụng trong app.js
module.exports = router;
