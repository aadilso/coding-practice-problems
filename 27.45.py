# Sometimes numbers are converted to words, like in a wedding invitation. So 23 becomes "twenty three". Write a function DigitToWord that takes a single digit number from 0-9 and returns that number's word: 0 is zero, 1 is one, 2 is two, etc (if the number is outside 0-9, return "error"). Write another function TensDigitToWord that takes a single digit number from 2-9, and returns that number's word when it appears in the tens digit: 2 is twenty, 3 is thirty, etc. If the number is outside 2-9, return "error". Finally, write a function TwoDigitNumToWords that takes a two-digit number from 20-99 and returns that number in words. Your main program should get a user's integer, call TwoDigitNumToWords, and output the resulting string. If the input is 23, the output should be "twenty three".
#
# Do not do any error checking of the input. Note that your program does not support all numbers. 0-19 will yield error output, for example.
#
# HINTS:
#
# Write DigitToWord first, and test the function (have your main call that function directly) -- you won't pass any of the tests, but you should still start that way. Next, write TensDigitToWord and test it by itself also. Finally, write TwoDigitNumToWords (calling your first two functions) and test the entire program.
#
# Your TwoDigitNumToWords function should pass the ten's digit to TensDigitToWord. To get the tens digit, divide the number by 10.
#
# Your TwoDigitNumToWords function should pass the one's digit to DigitToWord. To get the ones digit, mod the number by 10 (num % 10).
#
# You can concatenate the strings returned by those two functions using the + operator. Ex: "hello" + " " + "there" yields one string "hello there".

def digit_to_word(digitIn):
    word_out = ""
    if digitIn == 0:
        word_out = ""
    elif digitIn == 1:
        word_out = "one"
    elif digitIn == 2:
        word_out = "two"
    elif digitIn == 3:
        word_out = "three"
    elif digitIn == 4:
        word_out = "four"
    elif digitIn == 5:
        word_out = "five"
    elif digitIn == 6:
        word_out = "six"
    elif digitIn == 7:
        word_out = "seven"
    elif digitIn == 8:
        word_out = "eight"
    elif digitIn == 9:
        word_out = "nine"
    else:
        word_out = "error"
    return word_out


def tens_digit_to_word(digitIn):
    word_out = ""
    if digitIn == 0:
        word_out = "error"
    elif digitIn == 1:
        word_out = "error"
    elif digitIn == 2:
        word_out = "twenty"
    elif digitIn == 3:
        word_out = "thirty"
    elif digitIn == 4:
        word_out = "forty"
    elif digitIn == 5:
        word_out = "fifty"
    elif digitIn == 6:
        word_out = "sixty"
    elif digitIn == 7:
        word_out = "seventy"
    elif digitIn == 8:
        word_out = "eighty"
    elif digitIn == 9:
        word_out = "ninety"
    else:
        word_out = "error"
    return word_out


def two_digit_num_to_words(num_in):
    ones_digit = num_in % 10
    tens_digit = num_in // 10
    return tens_digit_to_word(tens_digit) + " " + digit_to_word(ones_digit)


userNum = int(input())
print(two_digit_num_to_words(userNum))
