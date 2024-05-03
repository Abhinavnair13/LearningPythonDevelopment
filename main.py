import requests
import json

city = input("Enter the city for which you want ot see the weather ")
url = f"http://api.weatherapi.com/v1/current.json?key=84f6765d8ea9483fa4d70618240305&q={city}&aqi=no"
r = requests.get(url)

response_dict =json.loads(r.text)
print(response_dict['current']['temp_c'])
