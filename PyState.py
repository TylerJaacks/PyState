import urllib.request
import json

isu_cyride_prediction_endpoint = "http://webservices.nextbus.com/service/publicJSONFeed?a=cyride&command=predictions&stopId"
isu_dining_menu_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/menu/"
isu_dining_information = "http://apps.dining.iastate.edu/mystate-api/1.0/"

isu_dining_locations = {1 : "Conversations Dining", 
	4 : "Union Drive Marketplace",
	5 : "West Side Market",
	7 : "South Side Market",
	10 : "East Side Market",
	11 : "Business Caf\u00e9",
	12 : "Clyde\u0027s FRESH EXPRESS",
	13 : "Courtyard Caf\u00e9",
	14 : "Design Caf\u00e9",
	15 : "Gentle Doctor Caf\u00e9",
	16 : "Hawthorn",
	17 : "Hub Grill \u0026 Caf\u00e9",
	18 : "Caribou Coffee",
	30 : "ABE\u0027s Harvest Caf\u00e9",
	26 : "Froots",
	19 : "Memorial Union Food Court",
	21 : "Bookends Caf\u00e9",
	22 : "MU Market \u0026 Caf\u00e9",
	24 : "Seasons Marketplace",
	25 : "Storms Dining",
	28 : "Global Caf\u00e9",
	31 : "Friley Windows"}

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

request = urllib.request.Request("http://apps.dining.iastate.edu/mystate-api/1.0/menu/4") 
response = urllib.request.urlopen(request)

data = json.loads(response.read())

stations = []
fooditems = []

for object in data:
	stations.append(object["station"])

stations = remove_duplicates(stations)

print(stations)