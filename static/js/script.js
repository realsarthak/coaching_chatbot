function toggleChat() {
    const chatbot = document.getElementById("chatbot");
    chatbot.style.display = chatbot.style.display === "flex" ? "none" : "flex";
}

async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBody = document.getElementById("chat-body");
    const message = input.value.trim();

    if (!message) return;

    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.innerText = message;
    chatBody.appendChild(userDiv);

    input.value = "";
    chatBody.scrollTop = chatBody.scrollHeight;

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: message })
    });

    const data = await response.json();

    const botDiv = document.createElement("div");
    botDiv.className = "bot-message";
    botDiv.innerText = data.reply;
    chatBody.appendChild(botDiv);

    chatBody.scrollTop = chatBody.scrollHeight;
}

// Enter key support
document.addEventListener("DOMContentLoaded", () => {
    const input = document.getElementById("user-input");
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            sendMessage();
        }
    });
});