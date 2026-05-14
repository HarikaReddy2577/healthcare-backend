# Healthcare Backend API

A Django REST Framework backend for managing patients, doctors, and their assignments.

## Tech Stack
- **Django 5** + **Django REST Framework**
- **PostgreSQL** database
- **JWT Authentication** via `djangorestframework-simplejwt`
- **Docker** + **Docker Compose** for containerized deployment
- **GitHub Actions** CI/CD pipeline

---

## Quick Start (Local with Docker)

```bash
# 1. Clone and enter project
git clone <your-repo>
cd healthcare_backend

# 2. Start everything (DB + API)
docker-compose up --build

# 3. API is running at http://localhost:8000
```

---

## Quick Start (Local without Docker)

```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Setup .env (edit DB credentials)
cp .env .env.local

# 4. Create PostgreSQL DB
createdb healthcare_db

# 5. Run migrations
python manage.py migrate

# 6. Start server
python manage.py runserver
```

---

## API Endpoints

### Authentication
| Method | Endpoint | Auth | Description |
|--------|----------|------|-------------|
| POST | `/api/auth/register/` | ❌ | Register new user |
| POST | `/api/auth/login/` | ❌ | Login, get JWT token |

### Patients (Authenticated only)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/patients/` | Create patient |
| GET | `/api/patients/` | List my patients |
| GET | `/api/patients/<id>/` | Get patient detail |
| PUT | `/api/patients/<id>/` | Update patient |
| DELETE | `/api/patients/<id>/` | Delete patient |

### Doctors (Authenticated only)
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/doctors/` | Create doctor |
| GET | `/api/doctors/` | List all doctors |
| GET | `/api/doctors/<id>/` | Get doctor detail |
| PUT | `/api/doctors/<id>/` | Update doctor |
| DELETE | `/api/doctors/<id>/` | Delete doctor |

### Patient-Doctor Mappings
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/mappings/` | Assign doctor to patient |
| GET | `/api/mappings/` | List all mappings |
| GET | `/api/mappings/<patient_id>/` | Get doctors for a patient |
| DELETE | `/api/mappings/delete/<id>/` | Remove mapping |

---

## Sample API Requests (Postman)

### Register
```json
POST /api/auth/register/
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "SecurePass123!"
}
```

### Login
```json
POST /api/auth/login/
{
  "email": "john@example.com",
  "password": "SecurePass123!"
}
// Returns: { "tokens": { "access": "...", "refresh": "..." } }
```

### Create Patient (add Authorization: Bearer <token>)
```json
POST /api/patients/
{
  "name": "Alice Smith",
  "age": 30,
  "gender": "F",
  "phone": "9876543210",
  "email": "alice@example.com",
  "medical_history": "Diabetic"
}
```

### Assign Doctor to Patient
```json
POST /api/mappings/
{
  "patient": 1,
  "doctor": 1,
  "notes": "Primary care physician"
}
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | — |
| `DEBUG` | Debug mode | `True` |
| `DB_NAME` | PostgreSQL DB name | `healthcare_db` |
| `DB_USER` | PostgreSQL user | `postgres` |
| `DB_PASSWORD` | PostgreSQL password | — |
| `DB_HOST` | PostgreSQL host | `localhost` |
| `DB_PORT` | PostgreSQL port | `5432` |

---

## Project Structure
```
healthcare_backend/
├── healthcare_backend/     # Core settings, URLs
│   ├── settings.py
│   ├── urls.py
│   └── exception_handler.py
├── authentication/         # Register + Login (JWT)
├── patients/               # Patient CRUD
├── doctors/                # Doctor CRUD
├── mappings/               # Patient-Doctor assignment
├── .env                    # Environment variables (don't commit!)
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/      # CI/CD pipeline
    └── deploy.yml
```
