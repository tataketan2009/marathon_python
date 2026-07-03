import random

while True:  
    num = random.randint(1, 100)
    chances = 10  
    attempts = 0  
    game_won = False  

    print("\n--- New Game Started ---")
    print("You have 10 chances to guess the number!")

    while attempts < chances:
        guess = int(input(f"Attempt {attempts + 1}/{chances} - Guess a number between 1 and 100: "))
        attempts += 1  

        if guess == num:
            print("Congratulations! You guessed the number.")
            game_won = True
            break
        elif guess < num:
            print("Too low! Try again.")
        elif guess > num:
            print("Too high! Try again.")

    if not game_won:
        print(f"Game over! You've run out of chances. The correct number was {num}.")

    
    play_again = input("\nDo you want to play another game? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye.")
        break  
