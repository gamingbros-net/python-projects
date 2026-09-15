import random
import div
import time
import sys

symbols = ["🎲", "🔭", "💰", "⭐", "💸", "💎"]
balance = 100

def check_bet():
    global balance
    if bet > balance:
        print("You dont have enough balance!")
    elif bet <= 0:
        print("Please Enter a valid amount!")
    else:
        slot()

def output():
    global balance
    if slot_symbol_1 != slot_symbol_2 and slot_symbol_1 != slot_symbol_3 and slot_symbol_2 !=slot_symbol_3:
        print("Better Luck Next Time!")
        time.sleep(1)
        div.play_again()
    elif slot_symbol_1 == slot_symbol_2 == slot_symbol_3 == "🔭":
        print("You won an....")
        time.sleep(3)
        print("Audience with Herta herself")
        time.sleep(2)
        print('And a "little bit" of money')
        balance += bet*100
        time.sleep(1)
        div.play_again()
    elif slot_symbol_1 == slot_symbol_2 == slot_symbol_3 == "⭐":
        balance += bet*5
        print("JACKPOT!!!!")
        print(f"You Won ${bet*5}")
        time.sleep(1)
        div.play_again()
    elif slot_symbol_1 == slot_symbol_2 == slot_symbol_3:
        balance += bet*3
        print(f"You Won ${bet*3}")
        time.sleep(1)
        div.play_again()
    elif slot_symbol_1 == slot_symbol_2 or slot_symbol_2 == slot_symbol_3 or slot_symbol_1 == slot_symbol_3:
        balance += bet*1.5
        print(f"You Won ${bet*1.5}")
        time.sleep(1)
        div.play_again()

def slot():
    global balance
    balance -= bet
    print("Spinning...")
    time.sleep(2)
    print("***************")
    print("|", end="")
    for symbol in symbol_pool:
        print(symbol, end=" | ")
        time.sleep(1)
    print()
    print("***************")
    time.sleep(1)
    output()

print("----------------------------------")
print("Welcome to Penacony Gambling Slots")
print("Symbols:🎲 🔭 💰 ⭐ 💸 💎")
print("----------------------------------")
while True:
    symbol_pool = []
    slot_symbol_1 = random.choice(symbols)
    slot_symbol_2 = random.choice(symbols)
    slot_symbol_3 = random.choice(symbols)
    symbol_pool.extend([slot_symbol_1, slot_symbol_2, slot_symbol_3])
    print(f"Current balance: ${balance}")
    bet = input("Place your bet amount: ")
    bet = div.valid_float(bet, "Please enter a valid number!")
    if bet is None:
        continue
    check_bet()
    if balance <= 0:
        print("Oops, you lost all your money!")
        sys.exit()