# Contents
- [Run Locally](https://github.com/akashbose02/Tinkerquest/blob/main/backend/README.md#run-locally)
- [API Reference](https://github.com/akashbose02/Tinkerquest/blob/main/backend/README.md#api-references)

## Run Locally
```shell
# After cloning the project
cd backend/Tinker
pip install -r requirements.txt
python manage.py runserver
```

Go to `localhost:8000` to use the APIs

## API References

BASE URL = https://tinkerquest.onrender.com/

### Available endpoints
- dashboard/ `(GET)`
- signup/ `(POST)`
- login/ `(POST)`
- add-item/ `(POST)`
- edit-item/\<int:id>/ `(PUT)`
- delete-item/\<int:id>/ `(DELETE)`

### JSON Format Examples
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
- login/
```JSON
{
    "password": "9j20hvj0W\tc",
    "username": "debak"
}
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
- edit-item/5/
```JSON
{
    "threshold": 10,
}
```
- delete-item/5/
