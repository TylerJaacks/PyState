import urllib.request
import json

from enum import Enum

# Dining Locations
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

# Meal Types
class MealTypes(Enum):
	BREAKFAST = "Breakfast"
	LUNCH = "Lunch"
	DINNER = "Dinner"
	LATE_NIGHT = "Late Night"
	BAR_ONLY = "Deli/Salad Bar Only"
	CONTINUOUS_SERVICE = "Continuous Services"

# Laundry Rooms
class LaundryRoomLocations(Enum): 
	BARTON = "Barton"
	BUCHANAN = "Buchanan"
	EATON1 = "Eaton%201"
	EATON2 = "Eaton%202"
	EATON3 = "Eaton%203"
	EATON4 = "Eaton%204"
	ELM = "Elm"
	FREEMAN = "Freeman"
	FRILEY175A = "Friley%20175A"
	FRIELY84A = "Friley%2084A"
	GEOFFROY = "Geoffroy"
	HELSER = "Helser"
	LARCH = "Larch"
	LINDEN = "Linden"
	LYON = "Lyon"
	MAPLE = "Maple"

# MyState and NextBus endpoints.
isu_cyride_prediction_endpoint = "http://webservices.nextbus.com/service/publicJSONFeed?a=cyride&command=predictions&stopId="
isu_dining_hours_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/hours/"
isu_dining_menu_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/menu/"
isu_dining_information_endpoint = "http://apps.dining.iastate.edu/mystate-api/1.0/"
isu_laundry_endpoint="https://www.laundryalert.com/cgi-bin/backoffice/MachineState.py?format=JSON&loc=isulaundry&room="

# Remove duplicates in the lists.
def remove_duplicates(values):
	output = []
	seen = set()
	
	for value in values:
		if value not in seen:
			output.append(value)
			
			seen.add(value)
	return output

# Removes invalid characters from menus.
def remove_invalids(values):
	output = []

	for value in values:
		if value != "-":
			output.append(value)

	return output

# Retrieves JSON from a REST web service.
def get_JSON(url):
	request = urllib.request.Request(url) 
	response = urllib.request.urlopen(request)
	
	return json.loads(response.read())

# Gets food items from a specific dining location, and specific time.
def get_food_items(place, type):
	food_items = []

	data = get_JSON(isu_dining_menu_endpoint + str(place.value))

	for object in data:
		if object["event"] == str(type.value):
			food_items.append(object["item_main"])

	# TODO Does not remove duplicates.
	food_items = remove_duplicates(food_items)
	food_items = remove_invalids(food_items)

	if len(food_items) != 0:
		print(*food_items, sep='\n')
	else:
		print("None")

	return food_items

# Gets dining hours for a specific dining location.
def get_dining_hours(place, type):
	data = get_JSON(isu_dining_hours_endpoint + str(place.value))
	hours = ""

	for object in data:
		if object["name"] == str(type.value):
			hours = object["hours"]

	print(hours)

	return hours

def get_laundry(building):
	data = get_JSON(isu_laundry_endpoint + str(building.value))
	
	for object in data["location"]:
		location = data["location"]

		for object in location["rooms"]:
			print(location["rooms"])
			print("\n")

# TODO Get bus times.
def get_bus_times(stop_id):
	times = []

	data = get_JSON(isu_cyride_prediction_endpoint + str(stop_id))

	print("Stubbed!")