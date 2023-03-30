# Given a total amount of inches, convert the input into a readable output in feet and inches.
#
# Ex: If the input is:
#
# 55
# the output should be:
#
# 4'7"

inches = int(input())

feet = inches // 12
inches = inches - feet * 12

print(f"{feet}'{inches}\"")