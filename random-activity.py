
import requests

url = 'https://bored.api.lewagon.com/api/activity/'

responce = requests.get(url)
data = responce.json()

print("If you can not decide what to do with your spare time here is an activity for you:")
print(data['activity'])
