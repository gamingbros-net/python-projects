number = 11
middle = number // 2  # = 2

# Top half (including middle)
for i in range(middle + 1):
    spaces = " " * (middle - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

# Bottom half
for i in range(middle - 1, -1, -1):
    spaces = " " * (middle - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)