import requests
import simplejson


r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=london")

r = r.content

print(r)
