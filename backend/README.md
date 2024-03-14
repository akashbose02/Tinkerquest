# API Reference

## Available Endpoints
1. https://tinkerquest.onrender.com/api/skus
2. https://tinkerquest.onrender.com/api/inventory_items
3. https://tinkerquest.onrender.com/api/sales_orders
4. https://tinkerquest.onrender.com/api/stock_movements

## Examples

### GET Request for `https://tinkerquest.onrender.com/api/skus`
```JavaScript
fetch('https://tinkerquest.onrender.com/api/skus', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log('SKUs:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```

### POST Request for `https://tinkerquest.onrender.com/api/skus`
```JavaScript
const postData = {
  name: 'Blood Test Kit',
  description: 'Complete blood test kit including sample collection tubes, reagents, and instruction manual.',
  threshold: 50
};

fetch('https://tinkerquest.onrender.com/api/skus', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
.then(response => response.json())
.then(data => {
  console.log('Response:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```
<hr/>

### GET Request for `https://tinkerquest.onrender.com/api/inventory_items`
```JavaScript
fetch('https://tinkerquest.onrender.com/api/inventory_items', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log('Inventory Items:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```

### POST Request for `https://tinkerquest.onrender.com/api/inventory_items`
```JavaScript
const postData = {
  sku: 1, // Replace with appropriate SKU ID
  quantity: 100,
  location: 'Storage Room A',
  expiry_date: '2022-12-31' // Replace with appropriate expiry date
};

fetch('https://tinkerquest.onrender.com/api/inventory_items', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
.then(response => response.json())
.then(data => {
  console.log('Response:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```
<hr/>

### GET Request for `https://tinkerquest.onrender.com/api/sales_orders`
```JavaScript
  fetch('https://tinkerquest.onrender.com/api/sales_orders', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log('Sales Orders:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```

### POST Request for `https://tinkerquest.onrender.com/api/sales_orders`
```JavaScript
const postData = {
  items: [1, 2, 3], // Replace with appropriate Inventory Item IDs
  total_amount: 500.00
};

fetch('https://tinkerquest.onrender.com/api/sales_orders', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
.then(response => response.json())
.then(data => {
  console.log('Response:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```
<hr/>

### GET Request for `https://tinkerquest.onrender.com/api/stock_movements`
```JavaScript
fetch('https://tinkerquest.onrender.com/api/stock_movements', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json'
  }
})
.then(response => response.json())
.then(data => {
  console.log('Stock Movements:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```

### POST Request for `https://tinkerquest.onrender.com/api/stock_movements`
```JavaScript
const postData = {
  item: 1, // Replace with appropriate Inventory Item ID
  quantity_changed: -20
};

fetch('https://tinkerquest.onrender.com/api/stock_movements', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(postData)
})
.then(response => response.json())
.then(data => {
  console.log('Response:', data);
})
.catch(error => {
  console.error('Error:', error);
});

```
