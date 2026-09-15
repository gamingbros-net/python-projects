# Rock Paper Scissor Game

import random
import sys
while True: 
    win = {"rock":"scissor", "scissor":"paper", "paper":"rock"}
    lose = {"scissor":"rock", "paper":"scissor", "rock":"paper"}
    draw = {"scissor":"scissor", "paper":"paper", "rock":"rock"}
    score = 0
    round = 0
    while True:
        pick = ("rock", "paper", "scissor")
        opp_pick = random.choice(pick)
        print("--------------------------------------------")
        print(f"Round {round+1}")
        print(f"Score = {score}")
        rps = input("Enter (Rock/Paper/Scissor): ").lower()
        invalid = rps not in pick
        if invalid:
            print("Please Enter either Rock/Paper/Scissor")
        else:
            print(f"You Pick: {rps.capitalize()}")
            print(f"Opponent Picks: {opp_pick.capitalize()}")
            if win[rps] == opp_pick:
                print("You Win!")
                round += 1
                score += 1
            elif draw[rps] == opp_pick:
                print("It's A Draw!")
                print("Rematch!")
            elif lose[rps] == opp_pick:
                print("You Lose!")
                round += 1
            if round == 3:
                print(f"Your score: {score}")
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
            
