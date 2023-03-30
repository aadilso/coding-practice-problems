# Suppose a graphics program needs a function to indicate whether one rectangle is smaller than another rectangle. A rectangle is specified by its upper-left coordinate and bottom-right coordinate. If the first rectangle is (1, 1) and (2,3), and the second is (0,0) and (10,10), the function returns true.
#
# Hints:
#
# Use copy-paste to ensure your parameters exactly match the arguments. You can use the same names for parameters as the arguments.
#
# Declare local variables r1Area and r2Area to make your comparison expression simpler.
#
# Use the abs() function in cstdlib (requires #include ). # ignore this line its for c++
#
# Take great care to check and recheck that your calculations involve the correct values.

def first_rectangle_smaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr):
    r1_area = abs(r1xul - r1xbr) * abs(r1yul - r1ybr)
    r2_area = abs(r2xul - r2xbr) * abs(r2yul - r2ybr)

    return r1_area < r2_area


def main():
    r1xul = int(input())
    r1yul = int(input())
    r1xbr = int(input())
    r1ybr = int(input())
    r2xul = int(input())
    r2yul = int(input())
    r2xbr = int(input())
    r2ybr = int(input())

    if first_rectangle_smaller(r1xul, r1yul, r1xbr, r1ybr, r2xul, r2yul, r2xbr, r2ybr):
        print("The first rectangle is smaller.")
    else:
        print("The first rectangle is not smaller.")


if __name__ == '__main__':
    main()

