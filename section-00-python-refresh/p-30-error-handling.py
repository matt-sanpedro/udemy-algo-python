def divide(dividend, divisor):
    if divisor == 0:
        # create the exception object
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

grades = []

print("Welcome to the average grade program.")

# put code that might fail here
try:
    average = divide(sum(grades), len(grades))
# runs only if ZeroDivisionError is raised
except ZeroDivisionError as e:
    print(f"There are no grades to average. Error: {e}")
# runs only if the TRY block raises an exception that is not caught by the previous except block(s)
else:
    print(f"The average grade is {average}.")
# runs no matter what, even if an exception is raised and not caught
finally:
    # run this code no matter what
    print("Thank you")
