document.addEventListener('DOMContentLoaded', function(){
    const chatToggle = document.getElementById('chat-toggle');
    const chatWindow = document.getElementById('chat-window');
    chatToggle.addEventListener('click', function(){
        if(chatWindow.style.display === 'none' || chatWindow.style.display === ''){
            chatWindow.style.display = 'block';
        } else {
            chatWindow.style.display = 'none';
        }
    });

    const chatForm = document.getElementById('chat-form');
    const chatInput = document.getElementById('chat-input');
    const chatMessages = document.getElementById('chat-messages');

    chatForm.addEventListener('submit', function(e){
        e.preventDefault();
        const userMessage = chatInput.value.trim();
        if(userMessage !== ''){
            // Display user's message
            const messageElem = document.createElement('div');
            messageElem.classList.add('chat-message', 'user-message');
            messageElem.innerText = userMessage;
            chatMessages.appendChild(messageElem);
            chatInput.value = '';

            // Send the message to the Django endpoint
            fetch('/accounts/chatbot/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    // For production, include CSRF token as needed.
                },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                const botResponse = data.reply || "Sorry, something went wrong.";
                const botMessageElem = document.createElement('div');
                botMessageElem.classList.add('chat-message', 'bot-message');
                botMessageElem.innerText = botResponse;
                chatMessages.appendChild(botMessageElem);
                chatMessages.scrollTop = chatMessages.scrollHeight;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });
});
