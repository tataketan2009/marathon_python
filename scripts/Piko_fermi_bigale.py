import random

def generate_secret():
    digits = random.sample('0123456789', 3)
    if digits[0] == '0':
        digits[0] = random.choice('123456789')
    return ''.join(digits)


def save_high_score(new_score):
    with open('data/final_score.txt', 'w') as file:
        file.write(str(new_score)) 

secret = generate_secret()

print("Welcome to the Pico Fermi Bagel Game!")
print("I have thought of a 3-digit number. Try to guess it!")
print("Feedback:")
print("  Pico   → correct digit, wrong position")
print("  Fermi  → correct digit, right position")
print("  Bagel  → no digit correct")

high_score = 0
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
    print(secret)  # For debugging purposes, you can remove this line in production
    for i in range(3):
        if guess[i] == secret[i]:
            feedback.append("Fermi")
        elif guess[i] in secret:
            feedback.append("Pico")
    if not feedback:
        feedback.append("Bagel")

    print("Feedback:", " ".join(feedback))


#  CHECK THE HIGH SCORE AFTER THE GAME IS COMPLETED ---
print("\n========================================")
print(f"📊 Your final score: {attempts}")

# Compare the player's score with the high score from STEP 1
if attempts > high_score:
    print(f" NEW RECORD! You beat the old high score of {high_score}!") 
    save_high_score(attempts)  
    print(f" High score updated to {attempts}!")
else:
    print(f" Good game! The high score remains {high_score}.")
    print(f" You needed {high_score - attempts} more points to break the record.")