number = 7

while True:
    user_input = input("Would like to play (Y/n): ")
    
    if user_input == "n":
        break

    user_number = int(input("Guess the number: "))
    if user_number == number:
        print("You guessed it!")
        break
    elif abs(user_number - number) == 1:
        print("You were off by one.")
    else:
        print("Sorry, that's not correct.")
