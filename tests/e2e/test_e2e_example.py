import requests

def test_ping_service():
    resp = requests.get("https://api.github.com")
    assert resp.status_code == 200
