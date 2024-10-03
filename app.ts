// app.ts
document.getElementById('loginForm')?.addEventListener('submit', (event) => {
    event.preventDefault(); 

    const username = (document.getElementById('username') as HTMLInputElement).value;
    const password = (document.getElementById('password') as HTMLInputElement).value;

    // Simple validation
    if (username === 'testuser' && password === 'password123') {
        alert('Login successful!');
    } else {
        alert('Invalid username or password.');
    }
});
