# A user will enter an initial number, followed by that number of integers. Output those integers' sum. Repeat until the initial number is 0 or negative. Ex: If the user enters 3 9 6 1 0, the output is:
#
# 16
# Ex: If the user enters 3 9 6 1 2 5 3 0, the output is:
#
# 16
# 8
# Hints:
#
# Use a while loop as an outer loop. Get the user's initial number of ints before the loop, and at the end of the loop body.
#
# Use a for loop as an inner loop, inside the while loop body. Loop from i = 0, to i < (the number of ints).
#
# In the for loop, first read the next integer, then update the sum. After the for loop, output the sum.

intsSum = 0
userInt = 0

numInts = int(input())

while numInts > 0:
    intsSum = 0
    for i in range(numInts):
        userInt = int(input())
        intsSum += userInt
    print(intsSum)

    numInts = int(input())

# 3 9 6 1 0 -> 16
# 3 9 6 1 2 5 3 0 -> 16 8

