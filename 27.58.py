# Many documents require a specific format for listing a person's name. Assume you are given a person's full name (ie. first name, middle name, and last name). Output the full name in the following format: "lastName, firstName middleInitial.".
#
# Ex: If the input is:
#
# John Jane Doe
# the output should be:
#
# Doe, John J.

full_name = input().split()
first_name = full_name[0]
middle_initial = full_name[1][0]
last_name = full_name[2]

formatted_name = last_name + ", " + first_name + " " + middle_initial + "."
print(formatted_name)
