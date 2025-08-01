# Input contains three space separated numbers on the same line, X, Y and Z - the scores of students in three subjects.

# Read three space-separated scores from the user (X, Y, and Z)
x, y, z = map(float, input().split())

# Calculate the average of the three scores
avg = (x + y + z) / 3

# Print the average score
print(avg)

