# Employee Management System


## Local Development Setup

1. Clone the repository:
```bash
git clone <https://github.com/mdeibrahim/Employee_management_System.git>
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

### Using Postman

1. **Register a new user**
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/api/auth/signup/`
   - Headers: 
     ```
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "email": "user@example.com",
         "password": "yourpassword",
         "password2": "yourpassword"
     }
     ```

2. **Login to get JWT tokens**
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/api/auth/login/`
   - Headers:
     ```
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "email": "user@example.com",
         "password": "yourpassword"
     }
     ```
   - Save the `access` token from the response for subsequent requests

3. **Get User Profile**
   - Method: `GET`
   - URL: `http://127.0.0.1:8000/api/auth/profile/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     ```

4. **Create an Employer**
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/api/employers/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "company_name": "Example Corp",
         "contact_person_name": "John Doe",
         "email": "contact@example.com",
         "phone_number": "1234567890",
         "address": "123 Main St"
     }
     ```

5. **List All Employers**
   - Method: `GET`
   - URL: `http://127.0.0.1:8000/api/employers/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     ```

6. **Get Specific Employer**
   - Method: `GET`
   - URL: `http://127.0.0.1:8000/api/employers/<id>/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     ```

7. **Update Employer**
   - Method: `PUT`
   - URL: `http://127.0.0.1:8000/api/employers/<id>/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "company_name": "Updated Corp",
         "contact_person_name": "Jane Doe",
         "email": "updated@example.com",
         "phone_number": "0987654321",
         "address": "456 New St"
     }
     ```

8. **Delete Employer**
   - Method: `DELETE`
   - URL: `http://127.0.0.1:8000/api/employers/<id>/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     ```

9. **Logout**
   - Method: `POST`
   - URL: `http://127.0.0.1:8000/api/auth/logout/`
   - Headers:
     ```
     Authorization: Bearer <your_access_token>
     Content-Type: application/json
     ```
   - Body (raw JSON):
     ```json
     {
         "refresh": "<your_refresh_token>"
     }
     ```



## Environment Variables

The project uses the following environment variables (you can set them in a `.env` file):

```
DEBUG=True
SECRET_KEY=your-secret-key
```

## Contributing

1. Fork the repository
2. Create your feature branch 
3. Commit your changes 
4. Push to the branch 
5. Open a Pull Request
