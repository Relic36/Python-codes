Year = int(input("Enter a year: "))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")