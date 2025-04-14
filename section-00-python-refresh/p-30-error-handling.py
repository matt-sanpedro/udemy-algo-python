def divide(dividend, divisor):
    if divisor == 0:
        # create the exception object
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

grades = []

print("Welcome to the average grade program.")

try:
    average = divide(sum(grades), len(grades))
except ZeroDivisionError as e:
    print(f"There are no grades to average. Error: {e}")
else:
    print(f"The average grade is {average}.")
finally:
    # run this code no matter what
    print("Thank you")
