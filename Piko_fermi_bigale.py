import random

def generate_secret():
    digits = random.sample('0123456789', 3)
    if digits[0] == '0':
        digits[0] = random.choice('123456789')
    return ''.join(digits)

secret = generate_secret()

print("Welcome to the Pico Fermi Bagel Game!")
print("I have thought of a 3-digit number. Try to guess it!")
print("Feedback:")
print("  Pico   → correct digit, wrong position")
print("  Fermi  → correct digit, right position")
print("  Bagel  → no digit correct")

attempts = 0
while True:
    guess = input("Enter your guess (3 digits): ").strip()
    if len(guess) != 3 or not guess.isdigit():
        print("Invalid input. Please enter exactly 3 digits.")
        continue

    attempts += 1
    if guess == secret:
        print(f"Congratulations! You've guessed it in {attempts} tries!")
        break

    feedback = []
    #print(secret)  # For debugging purposes, you can remove this line in production
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("Fermi")
        elif guess[i] in secret:
            feedback.append("Pico")
    if not feedback:
        feedback.append("Bagel")

    print("Feedback:", " ".join(feedback))