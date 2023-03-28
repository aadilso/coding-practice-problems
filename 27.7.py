# A guitar has 6 strings that play the notes E (lowest), A, D, G, B, and e (highest). A guitar's neck has regions called frets. A musical chord like a "G" or "C" is a combination of notes, and can be played by pressing certain strings at certain frets and then strumming all 6 strings. To quickly learn to play chords, people share "tabs" -- visual indications of what strings to press. To enable easy sharing over the internet, tabs are usually shared as text files. Write a program that takes a string input representing one of three chords (G, C, D) and outputs the corresponding tab. If the input is G, the output is:
#
# e|-3-
# B|-0-
# G|-0-
# D|-0-
# A|-2-
# E|-3-
# 0 means to strum the string open (without pressing). 1 means to press the string at the first fret, 2 at the second fret, 3 at the third fret.
#
# If the input is C, the output is:
#
# e|-0-
# B|-1-
# G|-0-
# D|-2-
# A|-3-
# E|---
# The - on the E string below the numbers means to not strum that string for that chord.
#
# If the input is D, the output is:
#
# e|-2-
# B|-3-
# G|-2-
# D|-0-
# A|---
# E|---
# If the user enters an unrecognized chord like Am, the output should be: Am is not a supported chord.

userChord = input("Enter chord: ")  # Currently supported: G, C, D. Future chord may involve multiple characters, like Am.

if userChord == "G":
    print("e|-3-\nB|-0-\nG|-0-\nD|-0-\nA|-2-\nE|-3-")
    """
        e|-3-
        B|-0-
        G|-0-
        D|-0-
        A|-2-
        E|-3-
    """
elif userChord == "C":
    print("e|-0-\nB|-1-\nG|-0-\nD|-2-\nA|-3-\nE|---")
    """
        e|-0-
        B|-1-
        G|-0-
        D|-2-
        A|-3-
        E|---
    """
elif userChord == "D":
    print("e|-2-\nB|-3-\nG|-2-\nD|-0-\nA|---\nE|---")
    """
        e|-2-
        B|-3-
        G|-2-
        D|-0-
        A|---
        E|---
    """
else:
    print(userChord, "is not a supported chord.")