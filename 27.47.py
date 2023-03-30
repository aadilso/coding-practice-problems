# Money is a bit tricky to represent in programs. One naturally wants to use floating-point like 7.52 to represent 7 dollars and 52 cents,
# but many programmers believe that money should be represented as ints because money is counted (versus being measured like temperature).
# One approach is to do all money calculations using cents, represented as an integer, like 752 cents.
# A useful function in such an approach might convert cents into separate dollar and cents values.
# Write a function CentsToDollarsCents whose first parameter is given cents, and whose second and third parameters
# are dollars and remaining cents. If the first parameter is 752, the second parameter becomes 7 and the third 52.

def cents_to_dollars_cents(user_cents):
    num_dollars = user_cents // 100  # Ex: 752 // 100 is 7 (integer division ignores fraction)
    num_cents = user_cents % 100    # Ex: 752 % 100 is 52, because 752//100 is 7 remainder 52.
    return num_dollars, num_cents


user_cents = int(input())  # Ex: 752
num_dollars, num_cents = cents_to_dollars_cents(user_cents)

print(f"{num_dollars} dollars {num_cents} cents")

