# Given your current grade as the input, write a program to help you determine what score you need to get on a final to get an A (90% or higher) in a class.
# The syllabus states that the final is worth 40% of the overall grade.

currentGrade = float(input())
currentPoints = currentGrade * 0.6
pointsNeeded = 90 - currentPoints
gradeOnFinal = pointsNeeded / 40

print(f"{gradeOnFinal*100:.1f}%")

# 100 -> 75%
# 95 -> 82.5%
# 50 -> 150%



