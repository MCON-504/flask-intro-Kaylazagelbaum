from flask import Flask, requests

BASE = "http://localhost:5000"

print("Test 1: Welcome Route")
response = requests.get(f"{BASE}/")
print("Status Code:", response.status_code)
print("Content:", response.text)


print("Test 2: About Route")
response = requests.get(f"{BASE}/about")
print("Status Code:", response.status_code)
print("JSON:", response.json())

print("TEST 3: Greeting Route")
name = "Kayla"
response = requests.get(f"{BASE}/greet/{name}")
print("Status Code:", response.status_code)
print("Content:", response.text)
print("Contains name:", name in response.text())

print("TEST 4: Calculator Route")
response = requests.get(f"{BASE}/calculate?num1=10&num2=5&operation=add")
print("Add Result:", response.json())

response = requests.get(f"{BASE}/calculate?num1=10&num2=5&operation=multiply")
print("Multiply Result:", response.json())

print("TEST 5: Echo Route (POST)")
payload = {"message": "Hello Flask!"}
response = requests.post(f"{BASE}/echo", json=payload)
print("Status Code:", response.status_code)
print("JSON:", response.json())
print("Echoed:", response.json().get("echoed") is True)

print("TEST 6: Status Code Route")
response_200 = requests.get(f"{BASE}/status/200")
response_404 = requests.get(f"{BASE}/status/404")

print("200 Test:", response_200.status_code, response_200.text)
print("404 Test:", response_404.status_code, response_404.text)

print("TEST 7: Custom Header")
response = requests.get(f"{BASE}/")
custom_header = response.headers.get("X-Custom-Header")
print("Custom Header:", custom_header)

print("TEST 8: Error Handling Route")
response = requests.get(f"{BASE}/cause-error")
print("Status Code:", response.status_code)
print("Response:", response.text)