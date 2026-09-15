import math
while True:
    a = float(input("Enter a quadratic coefficient: "))
    if a != 0:
        break
    else:
        print("The coefficient of x^2 cannot be zero. Please enter a valid quadratic coefficient.")

b = float(input("Enter a linear coefficient: "))
c = float(input("Enter a constant term: "))

D = b**2 - 4*a*c
if D > 0:
    root1 = (-b +math.sqrt(D)) / (2*a)
    root2 = (-b -math.sqrt(D)) / (2*a)
    if a == 1:
        print(f"The roots of the quadratic equation x^2 + {float(b)}x + {float(c)} = 0 are : {float(root1)} and {float(root2)}")
    else:
        print(f"The roots of the quadratic equation {float(a)}x^2 + {float(b)}x + {float(c)} = 0 are : {float(root1)} and {float(root2)}")
elif D == 0:
    root = -b / (2*a)
    if a == 1:
        print(f"The root of the quadratic equation x^2 + {float(b)}x + {float(c)} = 0 is : {float(root)}")
    else:
        print(f"The root of the quadratic equation {float(a)}x^2 + {float(b)}x + {float(c)} = 0 is : {float(root)}")
else:
    if a == 1:
        print(f"The root of the quadratic equation x^2 + {float(b)}x + {float(c)} = 0 has no real roots.")
    else:
        print(f"The root of the quadratic equation {float(a)}x^2 + {float(b)}x + {float(c)} = 0 has no real roots.")

