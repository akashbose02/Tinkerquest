document.addEventListener("DOMContentLoaded", function() {
    fetchInventoryItems();
});

function fetchInventoryItems() {
    fetch('https://tinkerquest.onrender.com/api/inventory_items')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            populateTable(data);
            console.log(data);
        })
        .catch(error => {
            console.error('Error fetching inventory items:', error);
        });
}

function populateTable(inventoryItems) {
    var tableBody = document.getElementById("fact-body");
    tableBody.innerHTML = ""; // Clear existing rows

    inventoryItems.forEach(function(item) {
        var row = document.createElement("tr");
        row.innerHTML = `
            <td>${item.id}</td>
            <td id="quantity-${item.id}">${item.quantity}</td>
            <td>${item.location}</td>
            <td><button class="add-btn" data-id="${item.id}">Add</button></td>
        `;
        tableBody.appendChild(row);
    });

    // Add event listeners to the newly created buttons
    document.querySelectorAll(".add-btn").forEach(button => {
        button.addEventListener("click", () => {
            var itemId = button.getAttribute("data-id");
            incrementQuantity(itemId);
        });
    });
}

function incrementQuantity(itemId) {
    var quantityElement = document.getElementById(`quantity-${itemId}`);
    var currentQuantity = parseInt(quantityElement.textContent);
    currentQuantity += 1;
    quantityElement.textContent = currentQuantity;

    fetch(`https://tinkerquest.onrender.com/api/inventory_items/${itemId}`, {
        method: 'PUT', // Use PUT method to update existing item
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            quantity: currentQuantity // Send updated quantity to the API
        }),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Quantity updated successfully:', data);
    })
    .catch(error => {
        console.error('Error updating quantity:', error);
    });
}