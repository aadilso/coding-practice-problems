# Many websites let users make reservations (hotel, car, flights, etc.). When a user selects a date, the next day is often automatically selected (for hotel checkout, car return, flight return, etc.). Given a date in the form of three integers, output the next date. If the input is 1 15 2017, the output should be 1 16 2017. If the input is 8 31 2017, the output should be 9 1 2017. Ignore leap years.
#
# Hints:
#
# Group the months based on number of days. Then create an if-else statement for each case.
#
# Note that 12 (December) is a special case; after the last day, the next month is 1 (January) and is the next year.


userMonth = int(input())
userDay = int(input())
userYear = int(input())

if userMonth == 12 and userDay == 31:
    # Last day of year
    nextMonth = 1
    nextDay = 1
    nextYear = userYear + 1
elif (userMonth in [1, 3, 5, 7, 8, 10] and userDay == 31) or (userMonth in [4, 6, 9, 11] and userDay == 30) or (userMonth == 2 and userDay == 28):
    # Last day of month
    nextMonth = userMonth + 1
    nextDay = 1
    nextYear = userYear
else:
    # Normal case, just increment day
    nextMonth = userMonth
    nextDay = userDay + 1
    nextYear = userYear

print(nextMonth, nextDay, nextYear)


