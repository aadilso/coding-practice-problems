# In the modern day Gregorian Calendar, a year consists of 365 days. In reality, the earth takes a little longer to rotate around the sun. If we did not account for the additional time, the calendar would be off! To fix this problem, every 4 years a leap year takes place. A leap year is when there are 366 days in the year - an extra day, February 29th, is added to the calendar. The requirements for a given year to be a leap year are:
#
# 1) The year must be divisible by 4.
#
# 2) If the year is a century year (1700, 1800, etc.), the year must be evenly divisible by 400.
#
# Some example leap years are 1712, 1944, and 2000.
#
# Write a program that takes in a year and determines whether it is a leap year or not.
# Output "true" if the given year is a leap year and output "false" if the given year is not a leap year.

year = int(input())
leap_year = False

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False

if leap_year:
    print("true")
else:
    print("false")
