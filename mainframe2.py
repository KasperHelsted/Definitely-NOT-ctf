import requests

url = 'https://mainframe-flipping.wep.dk/login'

data = {
    'password': 'asd'
}

resp = requests.post(url, data=data)

print(resp.cookies)
