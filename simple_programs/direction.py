routes = ["north", "south", "east", "west"]

while True:
    chosen_exit = ""
    
    while chosen_exit not in routes:
        chosen_exit = input("Please choose a direction to exit: ").casefold()
        
        
        if chosen_exit == "quit":
            print("Game Over")
            break  
            
    if chosen_exit == "quit":
        break

    print("Aren't you glad you got out of there?")

    ask = input("Would you like to play again? (yes/no): ").casefold()
    if ask == "no":
        print("Game Over")
        break