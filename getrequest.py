import requests

# Define the URL of the API endpoint
url = "https://pokeapi.co/api/v2/pokemon/ditto"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    pokemon_data = response.json()
    print("Name:", pokemon_data['name'])
    print("Base experience:", pokemon_data['base_experience'])
    print("Abilities:", [ability['ability']['name'] for ability in pokemon_data['abilities']])
else:
    print("Failed to retrieve data:", response.status_code)
