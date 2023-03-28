# A user is asked to type a caption for a photo in a web form's text field.
# If the caption didn't end with a punctuation mark (. ! ?), a period should automatically be added.
# A common error is to end with a comma, which should be replaced by a period.
# Another common error is to end with two periods, which should be changed to one period
# (however, ending with three periods (or more) indicates elipses so should be kept as is). The corrected caption is output.
# If the input is "I like pie", the output is "I like pie." If the input is "I like pie!", the output remains "I like pie!"
# If the input is "Coming soon…", the output remains "Coming soon…"

userCaption = input()
lastIndex = len(userCaption) - 1
lastChar = userCaption[lastIndex]

if lastChar in ['!', '?']:
    # Caption OK; do nothing
    pass
elif lastChar == ',':
    userCaption = userCaption[:lastIndex] + '.' # Replace ending , (common mistake) by .
elif lastChar != '.':
    # Not ! ? , . so append .
    userCaption += '.'
# check if last 2 are periods (..)
elif lastIndex > 0 and lastChar == '.' and userCaption[lastIndex - 1] == '.':
    # If just two periods
    if lastIndex > 1 and userCaption[lastIndex - 2] == '.':
        # Caption OK (ends with elipses ...  Do nothing
        pass
    else:
        # Ends with two periods; remove one
        userCaption = userCaption[:-1]

print(userCaption)