import requests
base_url = 'http://127.0.0.1:8000/api/'

name = 'Amiran'
surname = 'kalandia'
username = 'admin'
password = 'admin'

r = requests.get(f'{base_url}morning_shifts/') 
shifts = r.json()


shift_id = shifts[1]['id']
r = requests.post(f'{base_url}shift/{shift_id}/enroll/{name}', auth=(username, password))

if r.status_code == 200:
	print('Success')
	print(r.json()['text'])
elif r.status_code == 401:
	print('You are not Authenticated')

else:
	print('Erro occured while getting data')
