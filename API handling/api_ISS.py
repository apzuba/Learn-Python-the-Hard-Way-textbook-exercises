import requests
import json

response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)


print(response.json())


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())


parameters = {
    "lat": 50.063,
    "lon": 19.973
}

response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)

jprint(response.json())