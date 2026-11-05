import requests

url = "https://manning.com"
response = requests.get(url)
print(response.text)