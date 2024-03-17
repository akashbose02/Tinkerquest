function signup() {
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('signupPassword').value;
  
    // Check if any of the fields are empty
    if (!username || !email || !password) {
      alert("Please fill in all fields");
      return;
    }
    const data={
        "password": password,
        "username": username,
        "email": email,
        "date_joined": "2024-03-16",
        "password1": password,
        "password2": password
    }
    
    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data)
    };
    fetch('https://tinkerquest.onrender.com/signup/', options)
    .then(response => {
        if (response.status >= 200 && response.status < 300) {
            console.log("Successful signup");
            alert("Successful SignUp \n Now you can Login");
            window.location.href = 'login.html';
            return response.json(); // Return the JSON response for further processing
        } else {
            console.log("Signup failed");
            throw new Error("Signup failed"); 
            alert("Err0r Signing Up"); // Throw an error to be caught by the catch block
        }
    })
    .then(data => {
        // Process the JSON response data if needed
        console.log(data);
    })
    .catch(err => console.error(err));

      
    // fetch('https://tinkerquest.onrender.com/signup/', options)
    //     .then(response => response.json())
    //     .then(response => console.log(response))
    //     .catch(err => console.error(err));
  }
  
  // Attach event listener to the signup button
  document.getElementById('signup-button').addEventListener('click', signup);
  