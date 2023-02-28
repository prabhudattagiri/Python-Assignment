# g) create a list using names of 10 cities and pincodes. Combine them all to convert it into string 
# using join with delimiter “:”. Modify the names of cities by adding state-cities in the string. 
# Finally split it to have the information in list in the format state-city-pincode
# List of cities and their respective pincodes

cities = [ ("Mumbai", 400001),("Delhi", 110001),("Bengaluru", 560001),("Chennai", 600001),("Kolkata", 700001),("Hyderabad", 500001),
    ("Ahmedabad", 380001),("Pune", 411001),("Jaipur", 302001),("Lucknow", 226001),]

# Combine cities and pincodes into a string with ":" as delimiter
city_strings = []
for city, pincode in cities:
    city_strings.append(city + "-" + str(pincode))
combined_string = ":".join(city_strings)

# Create dictionary of city names and their respective states
city_state= {"Mumbai": "Maharashtra","Delhi": "Delhi","Bengaluru": "Karnataka","Chennai": "Tamil Nadu","Kolkata": "West Bengal",
    "Hyderabad": "Telangana","Ahmedabad": "Gujarat","Pune": "Maharashtra","Jaipur": "Rajasthan","Lucknow": "Uttar Pradesh",}

# Modify city names in combined string to include their respective states
cityStatePin = []
for city in combined_string.split(":"):
    city_name, pincode = city.split("-")
    state_name = city_state[city_name]
    cityStatePin.append(state_name + "-" + city_name + "-" + pincode)
    
print(cityStatePin)
