const stocksLink = document.getElementById('stocks-link');

stocksLink.addEventListener('click', function(event) {
  event.preventDefault(); // Prevent default link behavior

  // Create a new element for the message
  const message = document.createElement('div');
  message.classList.add('message'); // Add a class for styling

  // Add content and button
  message.innerHTML = 'This feature is empty for now!<br> We are working on it!!<br> It will be available soon.<br> <button class="ok-button">OK</button>';

  // Append the message element to the body
  document.body.appendChild(message);

  // Get the OK button
  const okButton = message.querySelector('.ok-button');

  okButton.addEventListener('click', function() {
    message.remove(); // Remove the message when OK is clicked
  });
});
