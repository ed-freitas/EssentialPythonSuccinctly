import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Define the data to be sent in the POST request
data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

# Make the POST request
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 201:
    # Parse the JSON response
    post_data = response.json()
    print("Created Post ID:", post_data['id'])
else:
    print("Failed to create post:", response.status_code)
