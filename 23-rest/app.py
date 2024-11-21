import requests
from flask import Flask, render_template
import json

url = "https://api.nasa.gov/planetary/apod"
FILE = open("key_nasa.txt", "r")
api_key = FILE.read()

dic = {
    "api_key": api_key
}

response = requests.get(url, dic=dic)

data = response.json()
print("Nasa Title!:", data['title'])
print("Here's what it does':", data['explanation'])
print("And here's an image to go along with it!:", data['url'])
