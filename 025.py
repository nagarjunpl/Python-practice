# Take matrix size from user
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Take matrix input from user
matrix = []
print("Enter the elements row by row:")
for i in range(rows):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    while len(row) != cols:
        print(f"Please enter exactly {cols} numbers.")
        row = list(map(int, input(f"Row {i+1}: ").split()))
    matrix.append(row)

# Display the matrix
print("\nMatrix:")
for r in matrix:
    print(r)

# Take user input for row & column to access
row_index = int(input("\nEnter row number to access (1-based index): ")) - 1
col_index = int(input("Enter column number to access (1-based index): ")) - 1

# Validate and display result
if 0 <= row_index < rows and 0 <= col_index < cols:
    print(f"Element at row {row_index+1}, column {col_index+1} is: {matrix[row_index][col_index]}")
else:
    print("Invalid row or column number.")
