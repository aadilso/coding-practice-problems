# Given an input positive integer, output each digit on its own line, starting with the rightmost digit. Ex: If the input is 935, the output is:
#
# 5
# 3
# 9
# Use the mod operator (%) to get the rightmost digit.
#
# Mod by 10 to get the rightmost digit.
#
# Use a loop that keeps a current dividend (the number being divided). In each iteration, output the rightmost digit, then update the divisor by dividing by 10.
#
# End the loop when the divisor is 0.

userInt = int(input())
divisor = userInt
while divisor != 0:
    print(divisor % 10) # print the right most digit
    divisor = divisor // 10  # // means floor division this will remove the right most digit eg. for 935: 935 -> 93 then 93 > 9 then 9//10 becomes 0
