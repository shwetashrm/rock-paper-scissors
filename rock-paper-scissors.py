import random

print("Welcome to Rock, Paper, Scissors game!\n")
print("Choose your move:\n1. Rock\n2. Paper\n3. Scissors")

# Define a function to get the user's move
def get_player_move():
    move = input("Enter the number of your move: ")
    while move not in ["1", "2", "3"]:
        move = input("Invalid input. Please enter the number of your move: ")
    return int(move)

# Define a function to get the computer's move
def get_computer_move():
    return random.randint(1, 3)

# Define a function to determine the winner
def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return "Tie"
    elif player_move == 1 and computer_move == 3:
        return "Player wins!"
    elif player_move == 2 and computer_move == 1:
        return "Player wins!"
    elif player_move == 3 and computer_move == 2:
        return "Player wins!"
    else:
        return "Computer wins!"

# Main game loop
while True:
    player_move = get_player_move()
    computer_move = get_computer_move()
    print("You chose: ", player_move)
    print("Computer chose: ", computer_move)
    print(get_winner(player_move, computer_move))
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break

print("Thanks for playing!")
