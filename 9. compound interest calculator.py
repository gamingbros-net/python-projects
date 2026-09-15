# Python compound interest calculator

while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle can't be less than or equal to zero")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest (in %): "))
    if rate <= 0 or rate > 100:
        print("Rate can't be less than or equal to zero or higher than 100%")
    else:
        break

while True:
    time = float(input("Enter the periods of time: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break

final_amount = principle*((1+(rate/100))**time)

print(f"Your final amount is ${final_amount:.2f}")

        
