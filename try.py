import random

num = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")

guess = int(input("Guess a number between 1 and 100: "))

while guess != num:
    if guess < num:
        print("Too low! Try again.")
    elif guess > num:
        print("Too high! Try again.")
    guess = int(input("Guess a number between 1 and 100: "))
    print("Congratulations! You guessed the correct number:", num) 
else:
    print("Invalid input. Please enter a number between 1 and 100.")