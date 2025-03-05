# global variables should be at the top
friends = []

def hello():
    print("Hello, World!")

hello()

def user_age_in_seconds(user_age_years):
    age_seconds = user_age_years * 365 * 24 * 60 * 60
    print(f"You are {age_seconds} seconds old.")

user_age_in_seconds(30)

def add_friend():
    friends.append("Rolf")

add_friend()
print(friends)
