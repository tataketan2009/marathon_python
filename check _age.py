year_ = float(input("Enter your birth year: "))
current_year = float(input("Enter the current year: "))

age = current_year - year_

if age < 18 :
    print("Your are not eligible to drive.")
elif age >= 18 and age < 100:
    print("You are eligible to drive.")
else:
    print("invalid command")


print(f"Your age is: {age}")