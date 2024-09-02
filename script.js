document.getElementById('mood-form').addEventListener('submit', function (event) {
    event.preventDefault();
    const mood = document.getElementById('mood').value;
    
    fetch('/get-advice', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ mood: mood }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('advice').innerText = data.advice;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
