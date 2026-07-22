import random

# --- STEP 1: READ the high score BEFORE the game starts ---
def get_high_score():
    try:
        with open('highscore.txt', 'r') as file:
            # Read the number and convert it to an integer
            return int(file.read())
    except FileNotFoundError:
        # If the file doesn't exist, return 0 as the default
        return 0
    except ValueError:
        # If the file is empty or has letters, return 0
        return 0

# --- STEP 2: WRITE the new high score to the file ---
def save_high_score(new_score):
    with open('highscore.txt', 'w') as file:
        file.write(str(new_score))  # Convert integer to string before saving

# Load the current champion score ---
high_score = get_high_score()
print(f"🏆 Welcome! The current high score to beat is: {high_score}")
print("----------------------------------------")

# PLAY THE GAME and track the player's score ---
choices = ['snake', 'water', 'gun']
player_score = 0
rounds_to_play = 10  

for round_num in range(1, rounds_to_play + 1):
    print(f"\n--- Round {round_num} ---")
    user = input("Choose Snake, Water, or Gun: ").lower().strip()
    
    # Validate input
    if user not in choices:
        print("Invalid choice! You lose this round.")
        computer = random.choice(choices)
    else:
        computer = random.choice(choices)
        print(f"Computer chose: {computer}")

        # Game Logic
        if user == computer:
            print("It's a Draw!")
        elif (user == "snake" and computer == "water") or \
             (user == "water" and computer == "gun") or \
             (user == "gun" and computer == "snake"):
            print(" You win this round!")
            player_score += 1  # Increase player's score
        else:
            print(" You lose this round!")

#  CHECK THE HIGH SCORE AFTER THE GAME IS COMPLETED ---
print("\n========================================")
print(f"📊 Your final score: {player_score}")

# Compare the player's score with the high score from STEP 1
if player_score > high_score:
    print(f" NEW RECORD! You beat the old high score of {high_score}!")
    save_high_score(player_score)  
    print(f" High score updated to {player_score}!")
else:
    print(f" Good game! The high score remains {high_score}.")
    print(f" You needed {high_score - player_score} more points to break the record.")