# (1) Given positive integer n, write a for loop that outputs the even numbers from n down to 0. If n is odd, start with the next lower even number. Hint: Use an if statement and the % operator to detect if n is odd, decrementing n if so.
#
# Enter an integer:
# 7
# Sequence: 6 4 2 0
# (2) If n is negative, output 0. Hint: Use an if statement to check if n is negative. If so, just set n = 0.
#
# Enter an integer:
# -1
# Sequence: 0
# Note: For simplicity add a space after each output value, including the last value.

userNum = int(input("Enter an integer:\n"))

print("Sequence: ", end="")

if userNum < 0:
    userNum = 0

if userNum % 2 == 1:  # Odd
    userNum -= 1

for i in range(userNum, -1, -2): # so from userNum to 0 with a step of -2 each time
    print(i, end=" ")