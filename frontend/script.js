
document.addEventListener('DOMContentLoaded', () => {
  const state = {};
  let context = null;
  let nodesToDestroy = [];
  let pendingUpdate = false;

  function destroyAnyNodes() {
    nodesToDestroy.forEach((el) => el.remove());
    nodesToDestroy = [];
  }

  function update() {
    if (pendingUpdate === true) {
      return;
    }
    pendingUpdate = true;

    document.querySelectorAll(".dynamic-content").forEach((el) => {
      // Update dynamic content based on state or context
      el.innerHTML = "<p>Dynamic content based on state or context.</p>";
    });

    destroyAnyNodes();

    pendingUpdate = false;
  }

  update(); // Initial update on page load
});
const url="https://tinkerquest.onrender.com/api/inventory_items";
fetch(url)
  .then(response => response.json())
  .then(data => {
    // Process the retrieved data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors that occurred during the request
    console.error('Error:', error);
  });