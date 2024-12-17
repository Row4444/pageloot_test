### To start project just use 
`./start.sh` 

There are 
#### Users
GET / POST `/api/users/` - to get users and create
PUT / DELETE `/api/users/{id}` - to update and delete user

POST data example
```json
    {
        "username": "SHREK",
        "email": "donk@dragon.com"
    }
```

#### Expenses

GET `/api/expenses/category_summary/?user_id={id}&month={Y}-{m}` - to get summary by category for user for month
GET `/api/expenses/date_range/?user_id={id}}&start_date={Y-m-d}&end_date={Y-m-d}` - to get expenses by date range for user

GET `/api/expenses/` Optional (`?user_id=2`)   - to get expenses (by user with user_id param)
POST `/api/expenses/` Optional (`?user_id=2`)   - to get expenses (by user with user_id param)

POST data example
```json
   {
      "user": 1,
      "title": "Villagers",
      "amount": 15,
      "date": "2024-12-17",
      "category": "Food"
  }
```

PUT / DELETE `/api/expenses/{id}` - to update and delete expense
