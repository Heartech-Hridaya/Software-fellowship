const BASE_URL = 'http://localhost:8000';

const registerForm = document.getElementById('registerForm');
const loginForm = document.getElementById('loginForm');
const messageDiv = document.getElementById('message');

function showMessage(msg, isError = false) {
  messageDiv.textContent = msg;
  messageDiv.className = isError ? 'error' : '';
}

registerForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const firstname = document.getElementById('firstname').value;
  const lastname = document.getElementById('lastname').value;
  const email = document.getElementById('registerEmail').value;
  const password = document.getElementById('registerPassword').value;

  try {
    const res = await fetch(`${BASE_URL}/register`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ firstname, lastname, email, password })
    });

    const data = await res.json();

    if (res.ok) {
      showMessage('Registration successful!');
      registerForm.reset();
    } else {
      showMessage(data.message || 'Registration failed.', true);
    }
  } catch (error) {
    showMessage('Network error during registration.', true);
  }
});

loginForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const email = document.getElementById('loginEmail').value;
  const password = document.getElementById('loginPassword').value;

  try {
    const res = await fetch(`${BASE_URL}/login`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    if (res.ok) {
      showMessage('Login successful!');
      loginForm.reset();
    } else {
      showMessage(data.message || 'Login failed.', true);
    }
  } catch (error) {
    showMessage('Network error during login.', true);
  }
});
