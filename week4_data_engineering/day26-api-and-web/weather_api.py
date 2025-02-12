import requests

# API endpoint
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.4050&daily=temperature_2m_max&timezone=Europe%2FBerlin"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data["daily"]["temperature_2m_max"])
else:
    print(f"Failed to fetch data: {response.status_code}")