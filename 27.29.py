# Traversing a vector to find the max (or min) is common. Given a vector of integers, output the maximum integer found in the vector. If the input is 4 3 8 2 6, the output is 8.
#
# Hints:
#
# Declare a variable named maxItem to hold the max value seen so far. Update that value if you ever see a larger value.
#
# Initialize that variable to any element's value, NOT to 0.

# NOTE BECAUSE THESE QUESTIONS ARE ASKED IN THE CONTEXT OF C++ AND PYTHON BY DEFAULT (UNLESS YOU USE NUMPY OR SOMETHING) DOES NOT HAVE VECTORS WE WILL USE ARRAYS
# AS THEY ARE SIMILAR TO VECTORS IN C++

numItems = int(input())
listItems = []

# Get items
for i in range(numItems):
    currItem = int(input())
    listItems.append(currItem)

maxItem = listItems[0] # Initializing to value 0 would be WRONG. Can initialize to any arbitrary element's value.
for i in range(numItems):
    if listItems[i] > maxItem:
        maxItem = listItems[i] # This item is max seen so far, so update the max

print(maxItem)
