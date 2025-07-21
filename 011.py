# Function to check if a given year is a leap year
def is_leap(year):
    leap = False  # Assume it's not a leap year initially

    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If divisible by 4, check if it's NOT divisible by 100 or divisible by 400
        if year % 100 != 0 or year % 400 == 0:
            leap = True  # It is a leap year

    return leap  # Return the result (True or False)

# Take input from the user
year = int(input("Enter a year: "))
# Print whether the year is a leap year or not
print(is_leap(year))
