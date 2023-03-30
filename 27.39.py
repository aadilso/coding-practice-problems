# Write a function called MaxFive that returns the maximum of five integer parameters. Ex: MaxFive(3, 5, 1, 0, 2) returns 5.
#
# Hints:
#
# Use four if statements. (Don't use if-else).
#
# Use a variable maxFound to keep track of the largest value seen so far.
#
# Initialize maxFound to one of the parameters. (Not to 0, which wouldn't handle the case when all parameters are negative).
#
# Don't forget to return maxFound.

def max_five(a, b, c, d, e):
    max_found = a  # Initializing to 0 would be wrong, what if all values are negative??

    if b > max_found:
        max_found = b
    if c > max_found:  # error if we used else if, rather than just if.
        max_found = c
    if d > max_found:
        max_found = d
    if e > max_found:
        max_found = e

    return max_found


v, w, x, y, z = map(int, input().split())
max_val = max_five(v, w, x, y, z)
print(max_val)


