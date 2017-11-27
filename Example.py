import PyState

# Get Food Items for Lunch at Conversations.
PyState.get_food_items(PyState.DiningLocations.CONVERSATIONS_DINING, PyState.MealTypes.LUNCH)

# Get Dining Hours for Lunch at Conversations.
PyState.get_dining_hours(PyState.DiningLocations.CONVERSATIONS_DINING, PyState.MealTypes.DINNER)

# Get Bus Data for Stop 1234.
PyState.get_bus_times(1234)

# Get Laundry Status for Buchanan.
PyState.get_laundry(PyState.LaundryRoomLocations.BUCHANAN)