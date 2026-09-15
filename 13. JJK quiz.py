import sys
questions = ("How many special grades sorcerer are there?: ",
             "What is principal Yaga cursed technique?: ",
             "How did Gojo die? (haha get spoilered): ",
             "What is Sukuna domain expansion called: ",
             "Black flash occurs when cursed energy is applied within how many seconds of a physical hit?: ")

options = (("A. 10", "B. 7", "C. 4",  "D. 8", "E. 5"),
           ("A. Cursed Corpse", "B. Limitless", "C. Ratio",  "D. Soul Transfiguration", "E. Blood Manipulation"),
           ("A. Punched to death", "B. Domain Expansion", "C. Blown up",  "D. World Cutting Slash", "E. Gojo never died (cope)"),
           ("A. Unlimited Void", "B. Self-Embodiment of Perfection", "C. Idle Death Gamble",  "D. Chimera Shadow Garden", "E. Malevolent Shrine"),
           ("A. 0.001 seconds", "B. 0.00001 seconds", "C. 0.000001 seconds",  "D. 0.0000001 seconds", "E. 0.0001 seconds"))

answers = ("E", "A", "D", "E", "C")
available = ("A", "B", "C", "D", "E")
guesses = []
while True:
    score = 0
    question_num = 0
    for question in questions:
        print("--------------------------------------------")
        print(f"Question number {question_num+1}")
        print(question)
        for option in options[question_num]:
            print(option)
        while True:
            guess = input("Type in Option Pick (A/B/C/D/E): ")
            invalid = guess.upper() not in available
            if invalid:
                print("Please type A/B/C/D/E")
            else:
                question_num += 1
                guesses.append(guess.upper())
                if guesses[question_num-1] == answers[question_num-1]:
                    score += 1
                    break
                else:
                    break
    print(f"You got {score} out of {question_num} right!")
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

