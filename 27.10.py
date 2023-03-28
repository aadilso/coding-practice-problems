# Airport runways are numbered using a 2-digit number, like 09.
# The meaning generally is that planes taking off or landing on that runway will be facing 090 or 90 degrees rotated right from north, namely facing east.
# Given a runway number (integer), output the degrees followed by the closest direction indication (north, northeast, east, southeast, south, southwest, west, or northwest). If the input is 03, the output is: 30 degrees (northeast).
#
# Hints:
#
# First just read the input number, multiply by 10 to yield runwayDeg.
#
# Next, create an if-else statement to compare runwayDeg's value with ranges for each direction. For north, the value should be within -22.5 and +22.5. For northeast, the value should be between 45 - 22.5 and 45 + 22.5. And so on.
#
# Based on the range in which the value falls, update a string variable with the direction. Then after the if-else, have a single output statement that outputs "270 degrees (north)" or whatever value and direction are correct.
#
# Don't forget that ranges use &&. An expression detecting a value x is between 1 and 10 is (x > 1) && (x < 10).
#
# Because the input is an integer which is multiplied by 10 to yield runwayDeg, the comparisons with floating-point values like 22.5 will never result in equality. Hence, the ranges don't have to account for such quality.


runwayNum = int(input())

runwayDeg = runwayNum * 10

runwayDirection = None # set to none originally

# Determine closest direction. Ranges are heading +/- 22.5.
if (runwayDeg > 0 - 22.5) and (runwayDeg < 0 + 22.5):
    runwayDirection = "north"
elif (runwayDeg > 45 - 22.5) and (runwayDeg < 45 + 22.5):
    runwayDirection = "northeast"
elif (runwayDeg > 90 - 22.5) and (runwayDeg < 90 + 22.5):
    runwayDirection = "east"
elif (runwayDeg > 135 - 22.5) and (runwayDeg < 135 + 22.5):
    runwayDirection = "southeast"
elif (runwayDeg > 180 - 22.5) and (runwayDeg < 180 + 22.5):
    runwayDirection = "south"
elif (runwayDeg > 225 - 22.5) and (runwayDeg < 225 + 22.5):
    runwayDirection = "southwest"
elif (runwayDeg > 270 - 22.5) and (runwayDeg < 270 + 22.5):
    runwayDirection = "west"
elif (runwayDeg > 315 - 22.5) and (runwayDeg < 315 + 22.5):
    runwayDirection = "northwest"

print(f"{runwayDeg} degrees ({runwayDirection})")
