# Given 10 input integers, output the minimum, maximum, and average of those integers. If the input is 1 1 1 1 1 3 3 3 3 3, the output is:
#
# 1 3 2
# If the input is 9 8 7 6 5 4 3 2 1 0, the output is:
#
# 0 9 4.5

userValues = []

for i in range(10):
    userValues.append(int(input()))

minVal = userValues[0] # Smallest seen so far
maxVal = userValues[0] # Largest seen so far
sumVals = 0

for i in range(10):
    curVal = userValues[i]

    if curVal < minVal: # Keep track of min
        minVal = curVal

    if curVal > maxVal: # Keep track of max
        maxVal = curVal

    sumVals += curVal # Keep track of sum for computing average later

print(minVal, maxVal, sumVals / 10.0)