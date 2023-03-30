# A list of 6 integers is input into vector listInts.
# Complete the program to copy only the negative integers to a new vector listNegInts.
# Output the number of negative elements, and the negatives list. Ex: For input 5 -2 0 9 -66 -4, output is:
# 3
# -2
# -66
# -4


listInts = [0] * 6
listNegInts = []

# Get input integers
for i in range(6):
    listInts[i] = int(input())

# Copy negative integers to new list
for i in range(6):
    if listInts[i] < 0: # Negative, so copy to other negatives list
        listNegInts.append(listInts[i])

# Output negative integers
print(len(listNegInts))
for i in range(len(listNegInts)):
    print(listNegInts[i])
