print("good morning")

n = int(input("Enter the number of players: "))

score = []

for i in range(n):
    player_score = int(input(f"Enter the score of player {i + 1}: "))
    if player_score > 6:
        print("Score cannot be greater than 6. Please enter a valid score.")
        player_score = int(input(f"Enter the score of player {i + 1}: "))
    score.append(player_score)

print("Scores:", score)


score.sort()
print("Sorted Scores:", score)

runner = score[-2]
print("Runner-up score:", runner)





