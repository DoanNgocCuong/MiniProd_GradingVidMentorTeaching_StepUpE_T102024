    // controllers/openAIController.js
const { getOpenAIResponse } = require('../services/openAIService');

exports.callOpenAI = async (req, res) => {
  const { systemPrompt, userInputPrompt } = req.body;

  if (!systemPrompt || !userInputPrompt) {
    return res.status(400).json({ error: 'System prompt và user input prompt không được để trống.' });
  }

  try {
    const response = await getOpenAIResponse(systemPrompt, userInputPrompt);
    res.json({ response });
  } catch (error) {
    console.error('Lỗi trong quá trình gọi OpenAI:', error);
    res.status(500).json({ error: 'Có lỗi xảy ra khi gọi OpenAI API.' });
  }
};
