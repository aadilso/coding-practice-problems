# Map/GPS applications commonly compute the distance between two points. A point may be a coordinate on an x-y plane like (1.5, 2.0).
# The distance formula is d = √((x2 - x1)2 + (y2 - y1)2) (basically, Pythagorean's Theorem).'
# ' Given two points, output the distance between them. If the input is (1.5, 2.0) (4.5, 6.0), the output is 5. Note: End with a newline.

import math

x1 = float(input("Enter num:\n"))
y1 = float(input("Enter num:\n"))
x2 = float(input("Enter num:\n"))
y2 = float(input("Enter num:\n"))

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(dist)
