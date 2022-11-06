import requests

dob_url = "https://api.thedogapi.com/v1/images/search"
response = requests.get(dob_url)

if response.status_code == 200:
    print(response.json())
else:
    print('실패')