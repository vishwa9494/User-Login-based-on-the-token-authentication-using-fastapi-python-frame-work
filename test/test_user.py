from fastapi.testclient import TestClient
from app.main import app

Client =TestClient(app)

def test_root():
    res=Client.get("/")
    print(res.json())


