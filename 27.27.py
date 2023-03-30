# Write a program that outputs the biggest difference (absolute value) between any successive pair of numbers in a list.
# Such a list might represent daily stock market prices or daily temperatures, so the difference represents the biggest single-day change.
# The input is the list size, followed by the numbers. If the input is 5 60 63 68 61 59, the output is 7.
# Hints:
#
# Declare a variable for the current number, and another for the previous number. At the start of each loop iteration, set prevNum = currNum, then get the next number into currNum.
#
# Maintain a max difference variable. Initialize it with 0. In each loop iteration, check if the difference between currNum and prevNum exceeds maxDiff; if so, update maxDiff with that difference.
#
# Don't forget to take the absolute value of the difference before the above comparison.
#
# Don't try to check the max difference for the first number in the list, since no previous number exists.

listSize = int(input())

maxDiff = 0
for i in range(listSize):
    currNum = int(input())
    if i > 0: # so if not the first num as we cant compare the number before that
        currDiff = abs(currNum - prevNum) # abs diff
        if currDiff > maxDiff:
            maxDiff = currDiff
    prevNum = currNum

print(maxDiff)
