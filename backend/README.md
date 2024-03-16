## API References

BASE URL = https://tinkerquest.onrender.com/

### Available endpoints
- dashboard/ `(GET)`
- signup/ `(POST)`
- login/ `(POST)`
- add-item/ `(POST)`
- edit-item/\<int:id>/ `(PUT)`
- delete-item/\<int:id>/ `(DELETE)`

### JSON Format and Code Examples
- dashboard/
```JS
const options = {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
  },
};

fetch('https://tinkerquest.onrender.com/dashboard/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
- signup/ (date format is YYYY-MM-DD)
```JSON
{
    "password": "9j20hvj0W\tc",
    "username": "debak",
    "email": "debak@example.com",
    "date_joined": "2024-03-16",
    "password1": "9j20hvj0W\tc",
    "password2": "9j20hvj0W\tc"
}
```
```JS
const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: '{"password":"9j20hvj0W\tc","username":"debak","email":"debak@example.com","date_joined":"2024-03-16","password1":"9j20hvj0W\tc","password2":"9j20hvj0W\tc"}'
};

fetch('https://tinkerquest.onrender.com/signup/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
- login/
```JSON
{
    "password": "9j20hvj0W\tc",
    "username": "debak"
}
```
```JS
const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: '{"password":"1234@abcd","username":"debak"}'
};

fetch('https://tinkerquest.onrender.com/login/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
- add-item/
```JSON
{
    "name": "PCR Reagents",
    "quantity": 50,
    "description": "Chemicals used in PCR tests to amplify and analyze DNA or RNA sequences.",
    "date_created": "2024-03-16T07:38:07.236123+05:30",
    "threshold": 10,
    "location": "Laboratory"
}
```
```JS
const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: '{"name":"Disposable Syringe","quantity":100,"description":"Syringe used for injecting a medicine or drawing off substances like blodd","date_created":"2024-03-16","threshold":20,"location":"Laboratory"}'
};

fetch('https://tinkerquest.onrender.com/add-item/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
- edit-item/5/
```JSON
{
    "threshold": 10,
}
```
```JS
const options = {
  method: 'PUT',
  headers: {
    'Content-Type': 'application/json',
  },
  body: '{"location":"Cold Storage Room"}'
};

fetch('https://tinkerquest.onrender.com/edit-item/7/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));

```
- delete-item/5/
```JS
const options = {
  method: 'DELETE',
  headers: {
    'Content-Type': 'application/json',
  },
};

fetch('https://tinkerquest.onrender.com/delete-item/7/', options)
  .then(response => response.json())
  .then(response => console.log(response))
  .catch(err => console.error(err));
```
