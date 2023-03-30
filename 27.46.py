# Driving is expensive. Write a function CostForMilesGas that takes miles driven and returns the cents, assuming 30 miles per gallon and a per gallon price of $4. Write a similar function CostForMilesMaintenance that assumes tires last 20,000 miles and cost $500, and that assumes $300 of service every 10,000 miles. Finally, write a function CostForMiles that takes miles driven, and calls those two functions, returning total cents. Use constants in the functions as appropriate, like MILES_PER_GAL, not hardcoded values in the function's statements. Use only integer arithmetic throughout. If the input is 50, the output should be: 941 cents
#
# Hints:
#
# Because you are only using integer arithmetic, do any divisions as late as possible, to reduce the impact of integer division ignoring fractions
#
# For gas, use an equation like this: centsGas = (milesDriven * CENTS_PER_GAL) / MILES_PER_GAL;
#
# For service, use an equation that starts like this: centsMaintenance = ((milesDriven * TIRES_CENTS) / TIRES_MILES) + … (Finish by adding a similar expression for service.

def cost_for_miles_gas(miles_driven):
    cents_gas = 0
    MILES_PER_GAL = 30
    CENTS_PER_GAL = 400

    cents_gas = (miles_driven * CENTS_PER_GAL) // MILES_PER_GAL
    # Note: Important to do the division last, because integer division ignores fraction.

    return cents_gas


def cost_for_miles_maintenance(miles_driven):
    cents_maintenance = 0
    # $500 every 20,000 miles for tires
    # $300 every 10,000 miles for service
    TIRES_CENTS = 50000
    TIRES_MILES = 20000
    SERVICE_CENTS = 30000
    SERVICE_MILES = 10000

    cents_maintenance = ((miles_driven * TIRES_CENTS) // TIRES_MILES) + (
                (miles_driven * SERVICE_CENTS) // SERVICE_MILES)

    # Note: Important to do the division last, because integer division ignores fraction.

    return cents_maintenance


def cost_for_miles(miles_driven):
    return cost_for_miles_gas(miles_driven) + cost_for_miles_maintenance(miles_driven)

miles_driven = int(input())

# 50 should give 941 cents
print(str(cost_for_miles(miles_driven)) + " cents")

