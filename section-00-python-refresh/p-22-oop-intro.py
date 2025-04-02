student = {"name": "Frodo", "grades": (89, 90, 93, 78, 90)}

# this function is "stand alone" from the student dictionary
def average(sequence):
    return sum(sequence) / len(sequence)

class Student:
    # self takes in the object that is being constructed
    def __init__(self, name, grades):
        # define the attributes of the class
        self.name = name
        self.grades = grades
        # define the average method inside the class

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

# create a thing from a class
# create an empty instance of the class
student = Student("Sam Gamgee", (90, 90, 93, 78, 90))
print(student.name) # access the name property
print(student.average_grade())
