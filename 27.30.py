# 12 values have been input into vector yearlyValues. Output all 12 elements, with 4 per line.
# If the elements are 10 20 30 40 50 60 70 80 90 100 110 120, the output is:

# 10 20 30 40
# 50 60 70 80
# 90 100 110 120

yearlyValues = []
for i in range(12):
    yearlyValues.append(int(input()))

# Output values, four per line
for i in range(0, 12, 4):
    print(yearlyValues[i], yearlyValues[i+1], yearlyValues[i+2], yearlyValues[i+3])
