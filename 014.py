''' Chef’s brain works correctly up to X bps. If he is currently working at Y bps, print YES if he is prone to errors (Y > X), otherwise print NO.
Input: Two space-separated integers X and Y
Output: Print YES or NO '''

# Input: two space-separated integers
X, Y = map(int, input().split())

# Check if current brain speed exceeds threshold
if Y > X:
    print("YES")  # Chef is prone to errors
else:
    print("NO")   # Chef is not prone to errors
