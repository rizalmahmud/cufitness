document.addEventListener('DOMContentLoaded', function() {
    // Function to retrieve a cookie value by name
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if this cookie string begins with the name we need
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', function(e) {
        e.preventDefault();
        const userMessage = chatInput.value.trim();
        if (userMessage) {
            // Append the user's message
            const userMessageDiv = document.createElement('div');
            userMessageDiv.classList.add('chat-message', 'user-message');
            userMessageDiv.innerText = userMessage;
            chatMessages.appendChild(userMessageDiv);
            chatInput.value = '';

            // Send message to the AI agent endpoint with CSRF token in headers
            fetch('/accounts/ai_agent/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')  // Include CSRF token here
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                // Process response
                const botReply = data.reply || "Sorry, something went wrong.";
                const botMessageDiv = document.createElement('div');
                botMessageDiv.classList.add('chat-message', 'bot-message');
                botMessageDiv.innerText = botReply;
                chatMessages.appendChild(botMessageDiv);
                // Scroll the chat window to the bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
            })
            .catch(error => {
                console.error("Error:", error);
            });
        }
    });
});
