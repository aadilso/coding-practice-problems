# Given a list of unique numbers, write a program that outputs Sorted if the numbers are in ascending order,
# Unsorted otherwise. If the input is 5 1 3 6 7 9, output Sorted.
# If the input is 3 10 8 2, output: Unsorted. A list of size 0 or 1 is sorted.

listSize = int(input())

isSorted = True
prevNum = 0
for i in range(listSize):
    currNum = int(input())
    if i > 0 and not currNum > prevNum:
        isSorted = False
    prevNum = currNum

if isSorted:
    print("Sorted")
else:
    print("Unsorted")
