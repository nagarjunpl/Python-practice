''' Write a program to print the grades of a student based on the marks he/she has obtained provided as input. 
The student is graded A if marks are greater than 90, B if marks are greater than 70, 
C if greater than or equal to 40, else F. '''

# Read the marks from the user
mark = int(input("Enter the student's marks: "))

# Check the grade based on the mark and print the corresponding grade
if mark > 90:
    print("A")  # Grade A for marks above 90

elif mark > 70:
    print("B")  # Grade B for marks between 71 and 90

elif mark >= 40:
    print("C")  # Grade C for marks between 40 and 70 (inclusive)

else:
    print("F")  # Grade F for marks below 40 (fail)
