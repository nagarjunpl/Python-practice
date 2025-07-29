''' You are given two integers a and b. Your task is to check whether the following condition is satisfied:
a + b + ( a × b ) = 111
If the condition is true, print "YES", otherwise print "NO". '''

# Take two integers as input from the user, separated by space
a, b = map(int, input().split())

# Calculate the expression: a + b + (a * b)
# Check if the result is equal to 111
if a + b + (a * b) == 111:
    # If the condition is true, print "YES"
    print("YES")
else:
    # Otherwise, print "NO"
    print("NO")
