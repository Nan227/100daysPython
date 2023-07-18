# Tic-Tac-Toe

# Function to print the game board
def print_board(board):
    print("-------------")
    for row in board:
        print("|", end=" ")
        for cell in row:
            print(cell, end=" | ")
        print("\n-------------")

# Function to check for a winning condition
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# Function to play the game
def play_game():
    # Create an empty game board
    board = [[" " for _ in range(3)] for _ in range(3)]

    # Variable to keep track of the current player
    current_player = "X"

    # Variable to keep track of the number of turns
    turns = 0

    while True:
        # Print the game board
        print_board(board)

        # Get the current player's move
        row = int(input("Enter the row (0-2): "))
        col = int(input("Enter the column (0-2): "))

        # Check if the move is valid
        if board[row][col] == " ":
            # Update the game board with the current player's move
            board[row][col] = current_player
            turns += 1

            # Check if the current player wins
            if check_win(board, current_player):
                print_board(board)
                print("Player", current_player, "wins!")
                break

            # Check if it's a tie
            if turns == 9:
                print_board(board)
                print("It's a tie!")
                break

            # Switch to the next player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")

# Start the game
play_game()
