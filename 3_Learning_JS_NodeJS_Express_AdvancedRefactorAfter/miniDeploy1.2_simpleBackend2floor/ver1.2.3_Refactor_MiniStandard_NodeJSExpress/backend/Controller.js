const express = require('express');
const axios = require('axios');
const dotenv = require('dotenv');
const cors = require('cors');

// Load environment variables from .env file
dotenv.config();

const app = express();
app.use(express.json());
app.use(cors());

const PORT = process.env.PORT || 3001;

// Helper function to send request to OpenAI API
const callOpenAI = async (systemPrompt, userInputPrompt) => {
    const apiKey = process.env.OPENAI_API_KEY;
    const url = 'https://api.openai.com/v1/chat/completions';
    
    const payload = {
        model: 'gpt-3.5-turbo',
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
        return response.data.choices[0].message.content;
    } catch (error) {
        throw new Error('Failed to call OpenAI API');
    }
};

// API endpoint to handle OpenAI requests
app.post('/api/openai', async (req, res) => {
    const { systemPrompt, userInputPrompt } = req.body;

    if (!systemPrompt || !userInputPrompt) {
        return res.status(400).json({ error: 'Both prompts are required.' });
    }

    try {
        const result = await callOpenAI(systemPrompt, userInputPrompt);
        res.json({ result });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
