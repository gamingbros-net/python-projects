import time
n = 4
#The foundational grid to lay all the numbers
grid = [[0] * n for _ in range(n)]

#Positional variable, will change for each new function
top = 0
left = 0
right = n - 1
bottom =  n - 1

#Value variable, for the result for each position in the grid
value = 1

#Display the grid after the code runs
def check():
    for row in grid:
        for val in row:
            print(val, end=" ")
        print()

#Main code and function to make the spiral, think of it as a robot that fills a spiral by observing if the closest top is smaller than the bottom or if the closest left is smaller than the right
while top <= bottom and left <= right:

    #TopLeft to TopRight
    for col in range(left, right + 1):
        grid[top][col] = value
        value += 1
    top += 1

    #TopRight to BottomRight
    for row in range(top, bottom + 1):
        grid[row][right] = value
        value += 1
    right -= 1

    #BottomRight to BottomLeft
    for inv_col in range(right, left - 1, -1):
        grid[bottom][inv_col] = value
        value += 1
    bottom -= 1

    #BottomLeft to TopLeft
    for inv_row in range(bottom, top - 1, -1):
        grid[inv_row][left] = value
        value += 1
    left +=1

check()