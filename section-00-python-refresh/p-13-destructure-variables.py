# tuples
x = (5, 11)

# the brackets are NOT necessary
y = 5, 11
print(f"{x}\n{y}")

# shorthand notation
a, b = x

# dictionary of student attendance
student_attendance = {"Jim": 96, "Frodo": 70, "Aragorn": 99}

# list of tuples
print(list(student_attendance.items()))

# list of tuples with three values
people = [("Jim", 45, "Mechanic"), ("Frodo", 70, "Ring bearer"), ("Aragorn", 99, "Swordsman")]

for name, age, profession in people:
    print(f"{name} is {age} years old and works as a {profession}")

# the "_" is a throwaway variable
for name, _, profession in people:
    print(f"{name} works as a {profession}")

# the "*" operator is used to unpack the rest of the values
head, *tail = list(range(1, 6))
print(head)
print(tail)
