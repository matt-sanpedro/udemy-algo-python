numbers = [1, 3, 5]
doubled = []

# regular for loop
for num in numbers:
    doubled.append(num*2)
print(doubled)

# list comprehension: good practice to keep variable in it short
doubled = [x*2 for x in numbers]
print(doubled)

# create a new list with friends that start with an s
friends = ["Rolf", "Sam", "Samantha", "Sarah", "Jenny"]
# start_with_s = [x[0].lower() == "s" for x in friends]    # returns boolean values

# list comprehension: must add the if statement at the end
start_with_s = [x for x in friends if x[0].lower() == "s"] #returns the names that start with s
print(start_with_s)

# for loop
start_with_s = []
for friend in friends:
    if friend.startswith("S"):
        start_with_s.append(friend)
print(start_with_s)

# regarding is statement: returns false since pointing to different memory allocation
print(start_with_s is friends)

# however: the elements are the same when using is keyword
print(start_with_s[0] is friends[0])

# print the memory address of a list with the id function
print(f"start_with_s: {id(start_with_s)}")
print(f"friends: {id(friends)}")

# to make two lists point to the same memory location
start_with_s = friends
