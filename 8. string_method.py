# validate user input exercise
# 1 username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

while True:
    username = input("Please enter a username: ")
    
    length = len(username)
    has_spaces = " " in username
    has_digits = not username.isalpha()
    
    if length <= 12 and not has_spaces and not has_digits:
        print(f"Welcome {username}!")
        break
    else:
        # Single error message covers all failures
        print("Invalid username. Must be ≤12 characters, no spaces, no digits.")