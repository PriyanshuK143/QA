var _a;
// app.ts
(_a = document.getElementById('loginForm')) === null || _a === void 0 ? void 0 : _a.addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;
    // Simple validation (in a real app, you would send this to a server)
    if (username === 'testuser' && password === 'password123') {
        alert('Login successful!');
    }
    else {
        alert('Invalid username or password.');
    }
});
