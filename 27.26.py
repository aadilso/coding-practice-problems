# A TV's size indicates the TV's diagonal. Thus, one 60" TV could have a different width and height than another 60" TV, both yielding a 60" diagonal.
# For a given TV diagonal, output a table listing possible widths and heights, each row increasing width by 1 inch. Only list rows where width is greater than height.
# Define diagonal, width, and height variables as doubles, but note that width will only take on rounded values like 20.0, 21.0, etc.

# Hints:
#
# Use Pythagorean's Theorem, solving for height.
#
# Write a for loop that iterates for widths ranging from 1 to the diagonal (you could define tighter bounds, but the program works with those looser bounds and is simpler).
#
# In the loop, compute the height for the given diagonal and width, using your height equation. Then use an if statement to output only if the width is greater than the height.


import math

tvDiagonal = int(input())

for tvWidth in range(1, tvDiagonal):
    tvHeight = math.sqrt((tvDiagonal * tvDiagonal) - (tvWidth * tvWidth))

    if tvWidth > tvHeight:
        print(tvWidth, tvHeight)

# input 54
# output:
# 39 37.3497
# 40 36.2767
# 41 35.1426
# 42 33.9411
# 43 32.665
# 44 31.305
# 45 29.8496
# 46 28.2843
# 47 26.5895
# 48 24.7386
# 49 22.6936
# 50 20.3961
# 51 17.7482
# 52 14.5602
# 53 10.3441

# input 60
# output:
# 43 41.845
# 44 40.7922
# 45 39.6863
# 46 38.5227
# 47 37.2961
# 48 36
# 49 34.6266
# 50 33.1662
# 51 31.607
# 52 29.9333
# 53 28.1247
# 54 26.1534
# 55 23.9792
# 56 21.5407
# 57 18.735
# 58 15.3623
# 59 10.9087

