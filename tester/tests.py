from tester.client import get

URL = "https://api.agify.io?name=michael"

def test_status():
    r, _ = get(URL)
    return r.status_code == 200

def test_json():
    r, _ = get(URL)
    return r.headers["Content-Type"].startswith("application/json")

def test_fields():
    r, _ = get(URL)
    data = r.json()
    return "name" in data and "age" in data

def test_types():
    r, _ = get(URL)
    data = r.json()
    return isinstance(data["age"], int)

def test_invalid():
    r, _ = get("https://api.agify.io")
    return r.status_code in [400, 422]

def test_latency():
    _, latency = get(URL)
    return latency < 3000
