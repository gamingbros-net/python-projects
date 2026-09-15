numbers = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for triples in numbers:
    for digits in triples:
        print(digits, end=" ")
    print()
