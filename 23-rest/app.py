import requests

url = "https://api.nasa.gov/planetary/apod"
key = open("key_nasa.txt", "r")
api_key = key.read()

dic = {
    "api_key": api_key
}

response = requests.get(url, dic=dic)

data = response.json()
print("Nasa Title!:", data['title'])
print("Here's what it does':", data['explanation'])
print("And here's an image to go along with it!:", data['url'])
