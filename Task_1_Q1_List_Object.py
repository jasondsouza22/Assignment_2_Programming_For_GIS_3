# Create a list of cities
cities = ["London", "Dubai", "New York", "Hong Kong", "Amsterdam"]

# Append a new city to the existing list
cities.append("Paris")

# Printing the length of the list
print("Length of the list:", len(cities))

# Removing an element at index 2 (which is 'Chicago') from the list
removed_city = cities.pop(2)

# Printing the updated list and the removed city
print("Updated list of cities: {}".format(cities))
print("Removed city: {}".format(removed_city))


