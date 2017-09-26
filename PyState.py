import urllib.request
import json

from enum import Enum

# Dining locations enums.
class DiningLocations(Enum):
	CONVERSATIONS_DINING = 1
	UNION_DRIVE_MARKETPLACE = 4
	WEST_SIDE_MARKET = 5
	SOUTH_SIDE_MARKET = 7
	EAST_SIDE_MARKET = 10
	BUSINESS_CAFE = 11
	CLYDES_FRESH_EXPRESS = 12
	COURTYARD_CAFE = 13
	DESIGN_CAFE = 14
	GENTLE_DOCTOR_CAFE = 15
	HAWTHORN = 16
	HUB_GRILL_CAFE = 17
	CARIBOU_COFFEE = 18
	ABE_HARVEST_CAFE = 30
	FROOTS = 26
	MEMORIAL_UNION_FOOD_COURT = 19
	BOOKENDS_CAFE = 21
	MU_MARKET_CAFE = 21
	SEASONS_MARKETPLACE = 24
	STORMS_DINING = 25
	GLOBAL_CAFE = 28
	FILEY_WINDOWS = 31

class MealTypes(Enum):
    BREAKFAST = "Breakfast"
    LUNCH = "Lunch"
    DINNER = "Dinner"
    LATE_NIGHT = "Late Night"
	CONTINOUS_SERVICE = "Continous Services" # TODO Fix spelling.

# Dining locations names.
isu_dining_locations = {
	1 : "Conversations Dining", 
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
	31 : "Friley Windows"
}

# MyState and NextBus endpoints.
isu_cyride_prediction_endpoint = "http://webservices.nextbus.com/service/publicJSONFeed?a=cyride&command=predictions&stopId"
isu_dining_hours_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/hours/"
isu_dining_menu_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/menu/"
isu_dining_information = "http://apps.dining.iastate.edu/mystate-api/1.0/"

# Remove duplicates in the lists.
def remove_duplicates(values):
    output = []
    seen = set()
    
    for value in values:
        if value not in seen:
            output.append(value)
            
            seen.add(value)
    return output

# Retrieves JSON from a REST web service.
def get_JSON(url):
	request = urllib.request.Request(url) 
	response = urllib.request.urlopen(request)
	
	return json.loads(response.read())

# Gets food items from a specific dining location.
def get_food_items(place):
    food_items = []
    
    data = get_JSON(isu_dining_menu_endpoint + str(place.value))
    
    for object in data:
        food_items.append(object["item_main"])

        food_items = remove_duplicates(food_items)

        print(*food_items, sep='\n')

    return food_items

# Gets food items from a specific dining location, and specific time.
def get_food_items(place, type):
	food_items = []

	data = get_JSON(isu_dining_menu_endpoint + str(place.value))

	for object in data:
        if object["event"] == str(type.value):
        food_items.append(object["item_main"])

	food_items = remove_duplicates(food_items)

	print(*food_items, sep='\n')

	return food_items

def get_dining_hours(place, type):
    data = get_JSON(isu_dining_hours_endpoint + str(place.value))

    return data[str(type.value)]

# TODO Get bus times.
def get_bus_times(stop_id):
	times = []

	data = get_JSON(isu_cyride_prediction_endpoint + str(stop_id))

	print(data)

get_food_items(DiningLocations.HAWTHORN)
get_food_items(DiningLocations.HAWTHORN, MealTypes.LUNCH)
get_dining_hours(DiningLocations.HAWTHORN, MealTypes.LUNCH)
