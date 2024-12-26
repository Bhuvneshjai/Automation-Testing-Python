import requests

# Wikipedia homepage URL
url = "https://www.wikipedia.org/"

# Define user agent
headers = {
    "User-Agent": "MyScraper/1.0 (https://mywebsite.com; myemail@example.com)"
}

# Fetch the homepage
response = requests.get(url, headers=headers)

# Check status and process
if response.status_code == 200:
    print("Page fetched successfully!")
    print(response.text[:500])  # Print first 500 characters of HTML
else:
    print("Failed to fetch page:", response.status_code)
