class App {
    constructor() {
        this.systemPromptEl = document.getElementById('systemPrompt');
        this.userInputPromptEl = document.getElementById('userInputPrompt');
        this.responseOutputEl = document.getElementById('responseOutput');
        this.submitButtonEl = document.getElementById('submitButton');

        this.bindEvents();
    }

    bindEvents() {
        this.submitButtonEl.addEventListener('click', () => this.handleSubmit());
    }

    async handleSubmit() {
        const systemPrompt = this.systemPromptEl.value.trim();
        const userInputPrompt = this.userInputPromptEl.value.trim();

        if (!systemPrompt || !userInputPrompt) {
            alert("Please fill in both fields!");
            return;
        }

        this.toggleLoading(true);

        try {
            const { result } = await API.callOpenAI(systemPrompt, userInputPrompt);
            this.displayResult(result);
        } catch (error) {
            this.displayResult(`Error: ${error.message}`);
        } finally {
            this.toggleLoading(false);
        }
    }

    displayResult(result) {
        this.responseOutputEl.textContent = result;
    }

    toggleLoading(isLoading) {
        this.submitButtonEl.disabled = isLoading;
        this.submitButtonEl.textContent = isLoading ? 'Processing...' : 'Submit';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new App();
});
