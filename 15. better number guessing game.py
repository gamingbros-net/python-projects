import random
import sys
while True:
    random_int = random.randint(1,100)
    attempts = 0
    guesses = ""
    while True:
        print("-------------------------------")
        guess = input("Pick a number from 1 to 100: ")
        if not guess.isnumeric():
            print("Please enter a whole number")
        elif 1 > int(guess) or int(guess) > 100:
            print("Please enter a number from 1-100")
        else:
            guess = int(guess)
            guesses += str(guess) + " "
            attempts += 1
            if guess < random_int:
                print("too low")
                print(f"guesses = {guesses}")
                print(f"remaining attempts = {7-attempts}")
            elif guess > random_int:
                print("too high")
                print(f"guesses = {guesses}")
                print(f"remaining attempts = {7-attempts}")
            else:
                print(f"Congratulations you win in {attempts} attempt/s!")
                break
            if attempts == 7:
                print(f"You lose! the right answer was {random_int}")
                break
    while True:
            play = input("Do you want to play again? (Y/N): ").lower()
            if play == "y":
                print("Good Luck!")
                break
            elif play == "n":
                print("Thankyou for Playing!")
                sys.exit()
            else:
                print("Please enter Y/N!")