# Commas make large integers easier to read. Ex: 145,020 is easier to read than 145020. Write a function that takes an integer, and returns a string representation of that number with commas appropriately inserted. If the input if 145020, the function returns string "145,020".
#
# Hints:
#
# Develop incrementally: Start by just converting the integer to a string, without commas. Then update the program to insert commas.
#
# This problem is hard. Take your time. Do little by little.
#
# Write a function to convert a single integer digit to a char (DigitToChar). Then use that function in your function that converts an integer to a string.
#
# Insert one digit at a time into the string, starting with the one's place. Use % 10 to get the rightmost digit. Use / 10 to shift the number right (discarding the current 1's place).
#
# Use the string's insert() function. Note that insert at the front has a strange syntax. For string str: str.insert(str.begin(), yourChar)

# Given int 0, 1, ... 9, returns ascii character '0', '1', ..., '9'.
def digit_to_char(single_digit):
    digit_as_char = '0'
    digit_as_char = chr(ord(digit_as_char) + single_digit)
    return digit_as_char


# Assuming a non negative user num ....
def num_to_comma_string(user_num):
    curr_num = user_num
    pos_count = 0  # Every 3 insert a comma
    num_as_string = ""

    while curr_num > 0:
        if pos_count == 3:
            num_as_string = ',' + num_as_string
            pos_count = 1  # 1 (not 0) because were going to add a digit
        else:
            pos_count += 1

        curr_digit = curr_num % 10  # Gets the rightmost digit eg. 569 % 10 is 9.
        curr_digit_as_char = digit_to_char(curr_digit)  # eg. 9 becomes '9'
        num_as_string = curr_digit_as_char + num_as_string
        curr_num = curr_num // 10  # Shifts the number right one digit. eg. 569 / 10 is 56.

    if user_num == 0:  # 0 is a special case; above loop never entered
        num_as_string = '0'

    return num_as_string

num = int(input())
print(num_to_comma_string(num))


