# Hangman game

import random
import sys
import div

while True:
    words = [
"Acheron",
"Aglaea",
"Argenti",
"Arlan",
"Asta",
"Aventurine",
"Bailu",
"Blade",
"Boothill",
"Clara",
"DrRatio",
"Feixiao",
"Firefly",
"Gallagher",
"Gepard",
"Guinaifen",
"Hanya",
"Herta",
"Himeko",
"Hook",
"Huohuo",
"Jade",
"Jiaoqiu",
"Jingliu",
"Kafka",
"Lingsha",
"Luka",
"Luocha",
"Lynx",
"Misha",
"Moze",
"Natasha",
"Pela",
"Qingque",
"Robin",
"Sampo",
"Seele",
"Serval",
"Sparkle",
"Sunday",
"Sushang",
"Tingyun",
"Topaz",
"Trailblazer",
"Welt",
"Xueyi",
"Yanqing",
"Yukong",
"Yunli"
]
    print("Welcome to Honkai:Star Rail Characters Hangman Game!")
    wordsp = random.choice(words)
    display = ""
    print(wordsp)
    for i in range(len(wordsp)):
        display += "_ "
    print(display)
    guessed_letter = ""
    guesses_so_far = ""
    attempts = 0
    while True:
        guess = input("Guess a letter: ").lower()
        invalid = not guess.isalpha()
        double = guess in guessed_letter
        more1 = len(guess) != 1
        if invalid:
            print("Enter a valid letter!")
        elif double:
            print("Letter have been used!")
        elif more1:
            print("Enter only 1 letter!")
        elif guess in wordsp.lower(): 
            guessed_letter += guess
        display = ""
        for letter in wordsp.lower():
            if letter in guessed_letter:
                display += letter + " "
            else:
                display += "_ "
        if not double and not invalid and not more1:
            doublew = guess in guesses_so_far
            if guess not in wordsp.lower() and not doublew:
                if guesses_so_far == "None":
                    guesses_so_far = ""
                guesses_so_far += guess + " "
                print("Oops it's wrong!")
                print(display)
                attempts += 1
                print(f"Total wrong attempts: {attempts}")
                print(f"Remaining attempts: {6-attempts}")
                print(f"Incorrect Guesses: {guesses_so_far}")
                if attempts >= 6:
                    print("You Lose!")
                    print(f"The correct guess was {wordsp}!")
                    break
            elif guess in wordsp.lower() and not doublew:
                print(display)
                print(f"Total wrong attempts: {attempts}")
                print(f"Remaining attempts: {6-attempts}")
                if guesses_so_far == "":
                    guesses_so_far += "None"
                    print(f'Incorrect Guesses: {guesses_so_far}')
                else:
                    print(f"Incorrect Guesses: {guesses_so_far}")
            else:
                print("Letter have been used!")
            if display.find("_") == -1:
                print(f"You win!") 
                print(f"The correct guess was {wordsp}")
                break
    div.play_again()