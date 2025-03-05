# dictionaries associate keys and values
friend_ages = {
    "Rolf": 30,
    "Stephanie": 27,
    "Kendrick": 34,
    "Juan": 31
}

print(friend_ages["Kendrick"])

# add a new key-value pair
friend_ages["Frodo"] = 111;
print(friend_ages)

# list of dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "John", "age": 36},
    {"name": "Jane", "age": 27}
]
print(friends)

# access index 1
print(friends[1]["name"])

# looping through
for friend, age in friend_ages.items():
    print(f"{friend}: {age}")

# check if a key exists in dictionary
print("Juan" in friend_ages)

# can also sum the values
age_values = friend_ages.values()
print(sum(age_values) / len(age_values))
