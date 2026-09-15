import sys
def play_again(message=""):
    while True:
        play = input("Do you want to play again? (Y/N): ").lower()
        if play == "y":
            if message:
                print(message)
            break
        elif play == "n":
            print("Thankyou for Playing!")
            sys.exit()
        else:
            print("Please enter Y/N!")

def valid_int(value, error_msg):
    try:
        return int(value)
    except ValueError:
        print(error_msg)
        return None
def valid_float(value, error_msg):
    try:
        return float(value)
    except ValueError:
        print(error_msg)
        return None
    
def valid_str(value, error_msg):
    if not value.isalpha():
        print(error_msg)
        return None
    else:
        return value

if __name__ == "__main__":
    play_again("")
