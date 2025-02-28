friends = ["Jim", "Karen", "Kevin", "Bob", "Kathy"]

for friend in friends:
    print(friend)

# range creates a list of numbers
for index in range(10):
    print(index)

# use a for loop to calculate the grades
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade
average = total / amount
print(average)

# using the sum function
average = sum(grades) / amount
print(average)
