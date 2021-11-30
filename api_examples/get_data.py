import requests
base_url = 'http://127.0.0.1:8000/api/'

r = requests.get(f'{base_url}morning_shifts/') 
shifts = r.json()


print(shifts)

