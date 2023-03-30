# The "mode" is a statistical summary of data (as are min, max, and average) representing the most commonly-occurring value. Given 10 integers ranging from 0 to 99, output the mode and its frequency. If the input is 1 1 1 1 2 2 9 8 7 6, the output is:
#
# 1 4
# If any integer is outside 0-99, output an error. If an input is 105, the output is:
#
# Invalid input: 105 is not in 0-99



userValues = [0] * 10
valCounts = [0] * 100

for i in range(10):
    userValues[i] = int(input())

    curVal = userValues[i]
    if curVal < 0 or curVal > 99:
        print("Invalid input: {} is not in 0-99".format(curVal))
        exit()

    valCounts[curVal] += 1

maxCount = valCounts[0]
maxCountIndex = 0
for i in range(1, 100): # Note to 100, not 10
    if valCounts[i] > maxCount:
        maxCount = valCounts[i]
        maxCountIndex = i

print(maxCountIndex, maxCount)