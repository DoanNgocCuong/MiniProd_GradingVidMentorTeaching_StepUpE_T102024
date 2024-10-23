// routes/openAIRoutes.js
const express = require('express');
const router = express.Router();
const openAIController = require('../controllers/openAIController');

// Định nghĩa API route
router.post('/openai', openAIController.callOpenAI);

module.exports = router;
