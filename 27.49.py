# Southern California's electric company uses a "three tier" cost structure for household electric bills. As of Jan 2017, for a given month, the first 232 kWh is $0.08291/kWh, the next 696 kWh is $0.16838/kWh, and any additional kWh is $0.23336/kWh. Write a function that takes a household month's kWh, and the cutoffs and prices for the tiers, and returns that month's electric cost.
#
# If the input is:
#
# 1700.0  232  0.08291 696  0.16838  0.23336
# the output is:
#
# $316.58
# Output each floating-point value with two digits after the decimal point, which can be achieved by executing
# cout << fixed << setprecision(2); once before all other cout statements.
#
# Hints:
#
# Think carefully through the logic of calculating the various cost contributions of each tier. We recommend calculating tier 3 first, then tier 2.
#
# Declare a variable named remainingKWh. Initialize it with the monthKWh. Also declare monthCost, initialized with 0.0. Declare tierKWh to use for computations.
#
# Start with an if statement if remainingKWh > (tier2Cutoff + tier1Cutoff). If yes, compute just the kWh that are part of tier 3, which is remainingKWh - (tier2Cutoff + tier1Cutoff), and store in tierKWh. Multiply tierKWh by tier3Cost, and add that to the monthCost. Then decrease remainingKWh by tierKWh.
#
# Repeat for tier2.
#
# For whatever is left in remainingKWh, multiply by tier1Cost.


def calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost):
    remaining_kwh = month_kwh
    month_cost = 0.0

    # month_kwh can be considered as having 3 parts on a number line: 1111122222222223333
    # (The number of 1s, 2s, and 3s above is arbitrary (just for illustrative purposes only)
    # the first branch below multiplies part 3 by tier3 cost
    # The second branch multiplies part 2 by tier2 cost
    # Finally part 1 is multiplied by tier1 cost

    if remaining_kwh > (tier2_cutoff + tier1_cutoff):  # Calculate the tier 3 amount
        tier_kwh = remaining_kwh - (tier2_cutoff + tier1_cutoff)
        month_cost += tier_kwh * tier3_cost  # The difference is the 3333 part above
        remaining_kwh -= tier_kwh  # This gets rid of the 3333 part, leaving the 11111222222222 part

    if remaining_kwh > tier1_cutoff:  # Calculate the tier 2 amount
        tier_kwh = remaining_kwh - tier1_cutoff
        month_cost += tier_kwh * tier2_cost  # The difference is the 2222222222 part
        remaining_kwh -= tier_kwh  # This gets rid of the 2222222222 part

    month_cost += remaining_kwh * tier1_cost  # The difference is the 11111 part above

    return month_cost


# try: 1700.0 , then 232 696 and on the last line 0.08291 0.16838 0.23336 -> should get $316.58
month_kwh = float(input())
tier1_cutoff, tier2_cutoff = map(float, input().split())
tier1_cost, tier2_cost, tier3_cost = map(float, input().split())

month_cost = calculate_month_electric_cost(month_kwh, tier1_cutoff, tier1_cost, tier2_cutoff, tier2_cost, tier3_cost)

print(f"${month_cost:.2f}")
