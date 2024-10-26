const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');
const cors = require('cors');

dotenv.config(); // Load biến môi trường từ file .env

const app = express();
app.use(express.json());
app.use(cors());

const PORT = process.env.PORT || 3001;

/**
 * Endpoint để gửi yêu cầu tới OpenAI API và trả về phản hồi
 */
app.post('/api/openai', async (req, res) => {
    const { systemPrompt, userInputPrompt } = req.body;

    if (!systemPrompt || !userInputPrompt) {
        return res.status(400).json({ error: 'System prompt và user input prompt không được rỗng.' });
    }

    const apiKey = process.env.OPENAI_API_KEY;
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
        res.json({ result: response.data.choices[0].message.content });
    } catch (error) {
        console.error('Lỗi trong quá trình gọi API:', error);
        res.status(500).json({ error: 'Lỗi trong quá trình gọi OpenAI API' });
    }
});

app.listen(PORT, () => {
    console.log(`Server đang chạy trên cổng ${PORT}`);
});
