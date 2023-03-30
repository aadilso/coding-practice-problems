# Compute the average of a list of user-entered integers representing rolls of two dice. The list ends when 0 is entered. Integers must be in the range 2 to 12 (inclusive); integers outside the range don't contribute to the average. Output the average, and the number of valid and invalid integers (excluding the ending 0). If only 0 is entered, output 0. The output may be a floating-point value. Ex: If the user enters 8 12 13 0, the output is:
#
# Average: 10
# Valid: 2
# Invalid: 1
# HINTS
#
# Use a while loop with expression (userInt != 0)
#
# Read the user's input into userInt before the loop, and also at the end of the loop body
#
# In the loop body, use an if-else to distinguish integers in the range and integers outside the range
#
# For integers in the range, keep track of the sum, and number of integers. For integers outside the range, just keep track of the number.
#
# Use a static cast to get a floating-point output: (static_cast (sum)) / num
#
# Whenever dividing, be sure to handle the case of the denominator being 0.


validSum = 0
validNum = 0
invalidNum = 0
userInt = int(input())
averageNum = 0.0

while userInt != 0:
    if 2 <= userInt <= 12:  # Valid
        validSum += userInt
        validNum += 1
    elif userInt != 0:  # Invalid
        invalidNum += 1

    userInt = int(input())

if validNum > 0:  # Avoid dividing by 0
    averageNum = float(validSum) / validNum

print("Average:", averageNum)
print("Valid:", validNum)
print("Invalid:", invalidNum)

# 8 12 13 0 -> avg: 10, valid:2,invalid:1
# 20 30 -1 -5 0 -> 0 , 0 , 4
# 2 2 3 3 0 -> 2.5,4,0

