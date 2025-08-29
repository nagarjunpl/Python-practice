# Q: What will be the final output after converting this list into a string?

a = ['Geeks', 'for', 'Geeks']

# Convert list to string using a loop
res = ''
for s in a:
    res += s + ' '

# Remove trailing space
res = res.strip()  
print(res)   # Expected output: "Geeks for Geeks"
