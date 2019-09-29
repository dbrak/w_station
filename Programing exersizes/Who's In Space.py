import requests
import simplejson
from prettytable import PrettyTable

r = requests.get("http://api.open-notify.org/astros.json")
r = r.content

js = simplejson.loads(r)

print("\nThere are",js["number"],"people in space now:")

t = PrettyTable(["Astronaut Name", "Space Craft",])

people = js["people"]
for person in people:
    t.add_row([person['name'],person['craft']])

print(t)
