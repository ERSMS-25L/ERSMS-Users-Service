import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from fastapi.testclient import TestClient
from main import app

print("DEBUG:", TestClient.__module__)  

client = TestClient(app)



def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_ready():
    response = client.get("/ready")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}

def test_get_user():
    response = client.get("/user/1")
    assert response.status_code == 200
    assert response.json() == {
        "user_id": 1,
        "name": "Fake User",
        "email": "test@example.com"
    }

