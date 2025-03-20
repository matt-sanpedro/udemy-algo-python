# like a list comprehension, but for dictionaries
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234"),
]

# want to create a mapping of user names to user information
username_mapping = {user[1]: user for user in users}
# keys in dictionary will be the usernames
print(username_mapping)

# now based on username, the data is easily accessible
print(username_mapping["Bob"])

# example of user input and unpacking the tuple
username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

try:
    _, username, password = username_mapping[username_input]
except KeyError:
    print(f"Username not found: {KeyError}")
    exit()

if password_input == password:
    print("Your details are correct!")
else:
    print("Incorrect credentials!")
