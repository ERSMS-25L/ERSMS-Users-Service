# ERSMS - User Service (Dummy)

This is a dummy User Service for development and testing.
It provides basic endpoints for health checks and user retrieval, used for integration with the API Gateway and other microservices.

## 🛠 How to Run Locally

```bash
uvicorn src.main:app --reload --port 8003
```

## 🐳 How to Build & Run with Docker

```bash
docker build -t user-service .
docker run -p 8003:8003 user-service
```

## 🌐 Endpoints

| Method | Endpoint         | Description           |
|--------|------------------|-----------------------|
| GET    | /health          | Health check          |
| GET    | /ready           | Readiness check       |
| GET    | /user/{user_id}  | Dummy user retrieval  |

EXAMPLE RESPONSE: 
{
  "user_id": 1,
  "name": "Fake User",
  "email": "test@example.com"
}

## ⚙️ Environment Variables

None required at this stage.

## 📦 Requirements

See `requirements.txt`

## 📁 Project Structure

```
user-service/
├── src/
│   └── main.py
├── tests/
├── .gitignore
├── requirements.txt
├── tests/
│ └── test_main.py
├── Dockerfile
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```
