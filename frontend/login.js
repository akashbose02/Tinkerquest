function login() {
  const enteredUsername = document.getElementById('name').value;
  const enteredPassword = document.getElementById('password').value;

  // Check if both username and password are entered
  if (!enteredUsername || !enteredPassword) {
    alert("Please enter both username and password");
    return; // Exit the function early if either field is empty
  }

  // Make a request to your API endpoint
  fetch('https://tinkerquest.onrender.com/login/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username: enteredUsername, password: enteredPassword })
  })
  .then(response => {
    if (response.ok) {
      // Successful login
      window.location.href = 'https://chat.openai.com/'; // Redirect to desired page
    } else {
      // Failed login
      alert("Invalid username or password");
    }
  })
  .catch(error => {
    console.error('Error:', error);
    alert("An error occurred during login");
  });
}

// Attach event listener to the login button
document.getElementById('login-button').addEventListener('click', login);
