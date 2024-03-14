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

  const url = "https://tinkerquest.onrender.com/api/inventory_items";

  const btnP = document.querySelector("#btn");
  const item = async () => {
    try {
      let response = await fetch(url);
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      let data = await response.json();
      const filteredData = data.filter(item => item.id === 1);
      displayData(filteredData);
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  };

  const displayData = (data) => {
    const factParagraph = document.getElementById("fact");
    factParagraph.innerHTML = ""; // Clear previous content
    data.forEach((item) => {
      const itemParagraph = document.createElement("p");
      itemParagraph.textContent = JSON.stringify(item); // Convert item to JSON string
      factParagraph.appendChild(itemParagraph);
    });
  };

  btnP.addEventListener("click", item);
});
