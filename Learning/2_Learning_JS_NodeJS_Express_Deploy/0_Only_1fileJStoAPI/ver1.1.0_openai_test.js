const axios = require('axios');
require('dotenv').config(); // Để lấy API Key từ file .env bằng cách gọi hàm config()
 
/**
 * Hàm để gửi yêu cầu tới OpenAI API và trả về phản hồi
 */
async function getOpenAIResponse(systemPrompt, userInputPrompt, apiKey) {
    if (!systemPrompt || !userInputPrompt) {
        throw new Error('System prompt và user input prompt không được rỗng.');
    }

    const url = 'https://api.openai.com/v1/chat/completions';

    const payload = {
        model: 'gpt-3.5-turbo', // Thay đổi mô hình nếu cần
        messages: [
            { role: 'system', content: systemPrompt },
            { role: 'user', content: userInputPrompt }
        ]
    };

    const options = {
        headers: {
            'Authorization': `Bearer ${apiKey}`,
            'Content-Type': 'application/json'
        }
    };

    try {
        const response = await axios.post(url, payload, options);
        console.log('Phản hồi từ OpenAI:', response.data.choices[0].message.content);
        return response.data.choices[0].message.content;
    } catch (error) {
        console.error('Lỗi trong quá trình gọi API:', error);
        throw error;
    }
}

// Chạy test
const systemPrompt = "You are a helpful assistant.";
const userInputPrompt = "What is the capital of France?";
const apiKey = process.env.OPENAI_API_KEY; // Thay bằng API key của bạn 

getOpenAIResponse(systemPrompt, userInputPrompt, apiKey);
