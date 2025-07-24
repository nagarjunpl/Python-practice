# Input: two space-separated integers
X, Y = map(int, input().split())

# Check if current brain speed exceeds threshold
if Y > X:
    print("YES")  # Chef is prone to errors
else:
    print("NO")   # Chef is not prone to errors
