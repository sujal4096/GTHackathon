document.getElementById('chat-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const message = document.getElementById('message').value;
    const responseBox = document.getElementById('response');

    const res = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: '123', message, lat: '0', lng: '0' }),
    });

    const data = await res.json();
    responseBox.innerText = data.response;
});