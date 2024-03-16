function login() {
    const username = document.getElementById('name').value;
    const password = document.getElementById('password').value;
  
    // Check if both username and password are entered
    if (!username || !password) {
      alert("Please enter both username and password");
      return; // Exit the function early if either field is empty
    }
  
    const data = {
      username: "debak",
      password: "1234@abcd"
    };
  
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    };
  
    fetch('https://tinkerquest.onrender.com/login/', options)
      .then(response => {
        if (response.ok) {
          // Successful login
          window.location.href = 'https://chat.openai.com/';
        } else {
          // Failed login
          console.log('Login failed');
        }
      })
      .catch(err => console.error(err));
  }
  
  // Attach event listener to the login button
  document.getElementById('login-button').addEventListener('click', login);
  