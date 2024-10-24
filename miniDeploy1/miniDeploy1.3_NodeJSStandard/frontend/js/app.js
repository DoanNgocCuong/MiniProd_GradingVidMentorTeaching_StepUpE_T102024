// frontend/js/app.js
document.getElementById('chat-form').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const systemPrompt = document.getElementById('systemPrompt').value;
    const userInputPrompt = document.getElementById('userInputPrompt').value;
    const responseDiv = document.getElementById('response');

    responseDiv.innerHTML = 'Đang xử lý...';

    try {
        const response = await fetch('http://localhost:3000/api/openai', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ systemPrompt, userInputPrompt })
        });

        const data = await response.json();
        if (response.ok) {
            responseDiv.innerHTML = `<p>${data.response}</p>`;
        } else {
            responseDiv.innerHTML = `<p>Lỗi: ${data.error}</p>`;
        }
    } catch (error) {
        responseDiv.innerHTML = `<p>Có lỗi xảy ra: ${error.message}</p>`;
    }
});
