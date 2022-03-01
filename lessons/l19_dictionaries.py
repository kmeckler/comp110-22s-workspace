"""Dictionaries."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key (lookup)
print(f"UNC has {schools['UNC']} students")

# Remove a key-value pair by its key
schools.pop("Duke")
print(schools)

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(is_duke_present)

# Update/reassign a value pair
schools["NCSU"] += 200
schools["UNC"] = 20000

print(schools)

# Error
# print(schools["Key"])

# Demonstration of dictionary literals
schools = {}  # same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {
    "UNC": 19400, 
    "Duke": 6717, 
    "NCSU": 26150
}
print(schools)

# When a key doesn't exist?
# print(schools["UNCC"])

# Looping over they keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")