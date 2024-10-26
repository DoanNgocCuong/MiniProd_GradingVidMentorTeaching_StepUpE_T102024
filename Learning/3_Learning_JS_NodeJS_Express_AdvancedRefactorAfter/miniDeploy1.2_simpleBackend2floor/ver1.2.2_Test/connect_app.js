async function callOpenAI() {
    const systemPrompt = document.getElementById('systemPrompt').value;
    const userInputPrompt = document.getElementById('userInputPrompt').value;

    if (!systemPrompt || !userInputPrompt) {
        alert("Vui lòng nhập đầy đủ cả hai trường!");
        return;
    }

    try {
        const response = await fetch('http://localhost:3001/api/openai', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                systemPrompt: systemPrompt,
                userInputPrompt: userInputPrompt
            })
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById('responseOutput').textContent = data.result;
        } else {
            document.getElementById('responseOutput').textContent = `Lỗi: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('responseOutput').textContent = `Lỗi khi gọi API: ${error}`;
    }
}
