class API {
    static BASE_URL = process.env.API_BASE_URL || 'http://localhost:3001';

    static async postRequest(endpoint, body) {
        const response = await fetch(`${this.BASE_URL}${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(body),
        });
        
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || 'API request failed');
        }
        return data;
    }

    static callOpenAI(systemPrompt, userInputPrompt) {
        return this.postRequest('/api/openai', { systemPrompt, userInputPrompt });
    }
}
