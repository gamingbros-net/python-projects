# Guessing numbers
import random

random_int = random.randint(1, 100)
attempts = 0  # Initialize attempts

while True:
    user_input = input("Guess a number between 1 and 100 (type 'i give up' to see the answer): ")
    
    # Check if they quit
    if user_input == "i give up":
        print(f"The number was: {random_int}")
        break
    
    # Convert input to integer
    try:
        user_input_int = int(user_input)
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    attempts += 1
    
    # Check if too close, too low, too high, or correct
    if abs(user_input_int - random_int) <= 5 and user_input_int != random_int:
        print("You're very close! Try again.")
    elif user_input_int > 100 or user_input_int <1:
        print("Please guess a number between 1 and 100!")
    elif user_input_int < random_int:
        print("Too low! Try again.")
    elif user_input_int > random_int:
        print("Too high! Try again.")
    else:  # user_input_int == random_int
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        if attempts <= 5:
            print("You're a genius!")
        elif attempts <= 10:
            print("You're pretty good!")
        else:
            print("You suck bruh")
        break
