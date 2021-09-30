import requests, json

# Do testing on main.py endpoint
request = requests.get('http://localhost:5000/').text
assert json.loads(request)["response"] == "Connected"