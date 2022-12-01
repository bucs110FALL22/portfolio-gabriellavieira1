import requests

response = requests.get('https://api.adoptapet.com/search/pets_at_shelter?key=A34F48&v=1&output=xml&shelter_id=2342')

print(response.status_code)
print(response.json)

species= response.json()['response'][0]['species']
print(species)

