# Formatting makes text easier for the viewer to read. Given a 10-digit phone number, output the number in a format that is easier for a person to read.
#
# Ex: If the input is:
#
# 1234567890
# the output should be:


number = input()
formatted_number = f"({number[:3]}) {number[3:6]}-{number[6:]}"
print(formatted_number)

