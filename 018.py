''' Alice has scored 
X
X marks in her test and Bob has scored 
Y
Y marks in the same test. Alice is happy if she scored at least twice the marks of Bob’s score. Determine whether she is happy or not. '''

# Read Alice's and Bob's scores
X, Y = map(int, input().split())

# Check if Alice's score is at least twice Bob's score
if X >= 2 * Y:
    # If the condition is true, Alice is happy
    print("YES")
else:
    # If the condition is false, Alice is not happy
    print("NO")
