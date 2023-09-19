# Create a dictionary of countries and their capitals
country_capitals = {
    "India": "Delhi",
    "Canada": "Ottawa",
    "UK": "London",
    "France": "Paris",
    "Germany": "Berlin"
}

# Print only the names of countries (keys)
print("Countries:", country_capitals.keys())

# Insert one more country and its capital
country_capitals["Australia"] = "Canberra"
print("New list:", country_capitals)

# Print the length of the dictionary
print("Length of the dictionary:", len(country_capitals))

# Remove an element from the dictionary (e.g., "Germany")
if "Germany" in country_capitals:
    del country_capitals["Germany"]

# Print the updated dictionary
print("Updated dictionary:", country_capitals)
