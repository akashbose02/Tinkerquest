// script.js
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