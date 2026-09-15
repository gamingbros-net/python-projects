import math
x = float(input("Enter a decimal: "))
y = float(input("Enter a negative number: "))

print(f"Rounded value: {round(x)}")
print(f"Value Rounded Up: {math.ceil(x)}")
print(f"Value Rounded Down: {math.floor(x)}")
print(f"Absolute value of the negative number you entered: {abs(y)}")
print(f"{x} raised to the power of 3: {pow(x, 3)}")

z = float(input("Enter another number: "))
print(f"The maximum of {x}, {y}, and {z} is: {max(x, y, z)}")
print(f"The minimum of {x}, {y}, and {z} is: {min(x, y, z)}")