// services/openAIService.js
const axios = require('axios');
require('dotenv').config();  // Đọc các biến môi trường từ tệp .env

const apiKey = process.env.OPENAI_API_KEY;
const url = 'https://api.openai.com/v1/chat/completions';

exports.getOpenAIResponse = async (systemPrompt, userInputPrompt) => {
  try {
    const response = await axios.post(
      url,
      {
        model: 'gpt-4o-mini',  // Có thể thay đổi nếu cần
        messages: [
          { role: 'system', content: systemPrompt },
          { role: 'user', content: userInputPrompt }
        ]
      },
      {
        headers: {
          'Authorization': `Bearer ${apiKey}`,
          'Content-Type': 'application/json'
        }
      }
    );

    return response.data.choices[0].message.content;
  } catch (error) {
    console.error('Lỗi khi gọi OpenAI API:', error.response ? error.response.data : error.message);
    throw new Error('Yêu cầu API thất bại.');
  }
};
