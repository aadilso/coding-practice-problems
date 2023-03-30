# Write a function that returns the index of the next occurrence of a substring in a string. Inputs are the string, start index, and substring.
# If not found, return -1. Do not use built-in string functions. If the input is "heyhey-friend", 1, "hey", the output is 3 (where the second "hey" starts).
#
# Hints:
#
# This is fairly difficult. You might start by writing a program that looks for a next single character rather than substring. Once that program is working and tested, then you're ready to look for a substring rather than a character.
#
# To look for a substring, consider writing a loop to do your own string comparison. Other approaches are possible.
#
# While you iterate through the string, realize that you can stop if you are near enough to the end that the substring can't possibly fit.
# So don't iterate all the way to i < string.size(); stop sooner than that.

def find_next_substr(string, start_index, substr):
    found_at_index = -1

    for i in range(start_index, len(string) - len(substr) + 1): # +1 as the range doesnt include the last value  ((7,19) does 7 to 18)
        substr_same = True

        for j in range(len(substr)):
            if string[i + j] != substr[j]:
                substr_same = False
                break
        if substr_same:
            found_at_index = i
            break

    return found_at_index


input_string = input()
start_index = int(input())
search_str = input()

print(find_next_substr(input_string, start_index, search_str))
