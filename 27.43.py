# Various websites like Wikipedia or IMDB list not just a person's birthdate but also the person's current age. Given a person's birthdate and current date, output the person's age in years. The custom is to round down. If the input is 7 1 2000 2 15 2015, the output is 14 (because the person hasn't yet reached their 15th birthday). A person less than 1 has age 0.
#
# Hints:
#
# Start by computing currAge just as the difference in years. Then, use an if-else statement to determine whether to decrement currAge.
#
# One reason to decrement is if the current month is less than the birth month (no birthday yet this year).
#
# Another reason to decrement is if the current month equals the birth month, but the current day is less than the birth day.


def get_age(birth_month, birth_day, birth_year, curr_month, curr_day, curr_year):
    curr_age = curr_year - birth_year

    # Check if birth month has been reached
    if curr_month < birth_month:
        curr_age -= 1
    # Check if birthday has been reached
    elif curr_month == birth_month and curr_day < birth_day:
        curr_age -= 1

    return curr_age


# Input format: birthMonth birthDay birthYear currMonth currDay currYear
birth_month, birth_day, birth_year, curr_month, curr_day, curr_year = map(int, input().split())

print(get_age(birth_month, birth_day, birth_year, curr_month, curr_day, curr_year))

