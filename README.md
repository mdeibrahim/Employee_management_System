# Employee Management System

A Django REST API for managing employees and employers with JWT authentication.

## Features

- Custom user authentication with JWT tokens
- CRUD operations for employers
- Secure endpoints with proper permissions
- Email-based authentication

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Local Development Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd employee-management-system
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

The server will start at `http://127.0.0.1:8000/`

## API Endpoints

### Authentication
- POST `/api/auth/signup/` - Register a new user
- POST `/api/auth/login/` - Login and get JWT tokens
- GET `/api/auth/profile/` - Get logged-in user's profile
- POST `/api/auth/logout/` - Logout (blacklist token)

### Employers
- POST `/api/employers/` - Create an Employer
- GET `/api/employers/` - List all Employers for the logged-in user
- GET `/api/employers/<id>/` - Retrieve a specific Employer
- PUT `/api/employers/<id>/` - Update a specific Employer
- DELETE `/api/employers/<id>/` - Delete a specific Employer

## Testing the API

You can use tools like Postman or curl to test the API endpoints. Here's an example using curl:

1. Register a new user:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/signup/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword", "password2": "yourpassword"}'
```

2. Login to get JWT tokens:
```bash
curl -X POST http://127.0.0.1:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "yourpassword"}'
```

3. Create an employer (using the access token from login):
```bash
curl -X POST http://127.0.0.1:8000/api/employers/ \
  -H "Authorization: Bearer <your_access_token>" \
  -H "Content-Type: application/json" \
  -d '{"company_name": "Example Corp", "contact_person_name": "John Doe", "email": "contact@example.com", "phone_number": "1234567890", "address": "123 Main St"}'
```

## Environment Variables

The project uses the following environment variables (you can set them in a `.env` file):

```
DEBUG=True
SECRET_KEY=your-secret-key
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 