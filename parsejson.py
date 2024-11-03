import requests

# Define the URL of the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    post_data = response.json()
    print("Post Title:", post_data['title'])
    print("Post Body:", post_data['body'])
else:
    print("Failed to retrieve data:", response.status_code)
