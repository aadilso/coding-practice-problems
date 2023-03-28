# An airline describes airfare as follows. A normal ticket's base cost is $300. Persons aged 60 or over have a base cost of $290.' \
# Children 2 or under have $0 base cost. A carry-on bag costs $10. A first checked bag is free, second is $25, and each additional is $50.
# Given inputs of age, carry-on (0 or 1), and checked bags (0 or greater), compute the total airfare.

passengerAge = int(input())
carryOns = int(input())
checkedBags = int(input())
airFare = 0

if passengerAge >= 60:
    airFare = 290  # Senior
elif passengerAge <= 2:
    airFare = 0  # Lap child
else:  # Regular: 2 < age < 60
    airFare = 300

if carryOns > 0:
    airFare += 10

if checkedBags == 2:
    airFare += 25
elif checkedBags >= 3:
    airFare += 25 + (checkedBags - 2) * 50  # 2nd bag is $25. Each bag beyond 2nd is $50
# Note: 0 or 1 bags is $0, so no adjustment to airfare

print(airFare)