# A user inputs the name of a shape (square or triangle). The program outputs the shape using asterisks. For input square, the output is:
#
# ***
# * *
# ***
# If the input is triangle, the output is:
#
#   *
#  * *
# *****

userShape = input()

if userShape == "square":
    print("***")
    print("* *")
    print("***")
elif userShape == "triangle":
    print("  *")
    print(" * *")
    print("*****")
else:
    print("Invalid input!")

