# An earlier problem introduced guitar tabs. In this problem, the user can enter a sequence of chords, and the program should output the tabs in sequence. The first input is the number of chords to follow. If the input is 4 G C G D, the output should be:
#
# e|-3-0-3-2-
# B|-0-1-0-3-
# G|-0-0-0-2-
# D|-0-2-0-0-
# A|-2-3-2---
# E|-3---3---
# Hints:
#
# Use 6 C++ strings, one for each guitar string ("string" below will mean C++ string unless otherwise noted).
#
# Start by the e string with "e|-", the B string with "B|-", etc.
#
# For each user chord, append (using append()) to each string the appropriate item (a number or -) plus -, like "2-".
#
# When done, print the 6 strings one at a time separated by newlines.

e_string = "e|-"
b_string = "B|-"
g_string = "G|-"
d_string = "D|-"
a_string = "A|-"
E_string = "E|-"

num_chords = int(input())

for i in range(num_chords):
    user_chord = input()
    if user_chord == "G":
        e_string += "3-"
        b_string += "0-"
        g_string += "0-"
        d_string += "0-"
        a_string += "2-"
        E_string += "3-"
    elif user_chord == "C":
        e_string += "0-"
        b_string += "1-"
        g_string += "0-"
        d_string += "2-"
        a_string += "3-"
        E_string += "--"
    elif user_chord == "D":
        e_string += "2-"
        b_string += "3-"
        g_string += "2-"
        d_string += "0-"
        a_string += "--"
        E_string += "--"

print(e_string)
print(b_string)
print(g_string)
print(d_string)
print(a_string)
print(E_string)