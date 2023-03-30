# Given a vector of digits (0-9) for a decimal number, write a function that returns a single integer. The 0'th element is the decimal number's one's place.
# If the vector's elements are 9, 6, 2, the function returns integer 269.
#
# Hints:
#
# First do the example conversion by hand to ensure you understand how each digit contributes to the total value of the integer.
#
# The first digit (at element 0) should be multiplied by 1, the second by 10, the third by 100, etc.
#
# Declare a variable to keep the total value (initialized with 0), and another to keep the current digit's weight (initialized with 1).
# For the current digit in the vector, multiply by the current weight and add to the total. Then update the weight in preparation for the next iteration.

def digits_to_num(digits_list):
    curr_weight = 1
    total_num = 0

    for digit in digits_list:
        total_num += digit * curr_weight
        curr_weight *= 10

    return total_num


digits_list = []

# read input digits from standard input
while True:
    user_input = input()
    if not user_input:
        break
    user_digit = int(user_input)
    digits_list.append(user_digit)

result_num = digits_to_num(digits_list)
print(result_num)
