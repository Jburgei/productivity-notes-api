# Productivity Notes API

A secure Flask RESTful API that allows users to register, log in, and manage their own personal notes.

This project implements **session-based authentication**, user-specific data access, full CRUD operations, and pagination.

---

##  Features

- User registration and login
- Session-based authentication
- Secure password hashing using bcrypt
- User-owned notes (each user can only access their own notes)
- Full CRUD functionality for notes
- Pagination support
- Database migrations using Flask-Migrate
- Seed script for test data

---

##  Tech Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- Marshmallow
- Flask-Bcrypt
- SQLite (development)

---

##  Authentication

This API uses **session-based authentication**.

- When a user logs in, their `user_id` is stored in Flask’s session
- The session is stored in an **encrypted cookie on the client**
- Protected routes check:
  ```python
  if not session.get("user_id"):
Project Structure
productivity-notes-api/
│
├── app.py
├── config.py
├── seed.py
├── models/
│   ├── user.py
│   └── note.py
├── routes/
│   ├── auth_routes.py
│   └── note_routes.py
├── migrations/
├── tests/
├── Pipfile
└── README.md
## Setup Instructions
1. Clone the repo
git clone git@github.com:Jburgei/productivity-notes-api.git
cd productivity-notes-api
2. Install dependencies
pipenv install
pipenv shell
3. Set environment variable
export FLASK_APP=app.py
4. Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
5. Run the app
flask run
API Endpoints
 Auth Routes
Signup
POST /signup
{
  "username": "joy",
  "password": "1234"
}
Login
POST /login
Check Session
GET /check_session
Logout
DELETE /logout
Notes Routes (Protected)
Create Note
POST /notes
Get Notes (Paginated)
GET /notes?page=1&per_page=10

Response:

{
  "items": [...],
  "page": 1,
  "pages": 1,
  "per_page": 10,
  "total": 1
}
Update Note
PATCH /notes/<id>
Delete Note
DELETE /notes/<id>
 Access Control
Each note belongs to a specific user (user_id)
Users cannot access or modify notes that are not theirs
Unauthorized access returns:
{
  "error": "Unauthorized"
}
Seeding Data

Run:

python seed.py

This will generate sample users and notes using Faker.

 Testing with curl

Example:

curl -c cookies.txt -X POST http://127.0.0.1:5000/login \
-H "Content-Type: application/json" \
-d '{"username": "joy", "password": "1234"}'


## Git Workflow

This project was developed using feature branches and pull requests:

feature/project-setup → initial structure
feature/app-setup → full backend implementation