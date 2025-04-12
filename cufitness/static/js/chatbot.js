document.addEventListener('DOMContentLoaded', function() {
    // Get references to the chat elements
    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    // Listen for form submission
    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            // Display user's message
            const userMessageDiv = document.createElement('div');
            userMessageDiv.className = 'chat-message user-message';
            userMessageDiv.innerText = userMessage;
            chatMessages.appendChild(userMessageDiv);
            chatInput.value = '';

            // Determine bot response using simple rules
            let botResponse = "";
            const lowerCaseMsg = userMessage.toLowerCase();
            if (lowerCaseMsg.includes("hi") || lowerCaseMsg.includes("hello")) {
                botResponse = "Hello! How can I help you today?";
            } else if (lowerCaseMsg.includes("help")) {
                botResponse = "Sure, I'm here to help. What do you need assistance with?";
            } else {
                botResponse = "I'm not sure I understand. Can you please rephrase?";
            }

            // Display bot's response
            const botMessageDiv = document.createElement('div');
            botMessageDiv.className = 'chat-message bot-message';
            botMessageDiv.innerText = botResponse;
            chatMessages.appendChild(botMessageDiv);

            // Scroll the chat window to the bottom
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    });
});
