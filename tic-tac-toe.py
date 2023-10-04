#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

# TODO: update the gameboard with the user input
def markBoard(position, mark):
    # Check if the position is valid and not already marked
    if position in board.keys() and board[position] == ' ':
        board[position] = mark
        return True
    else:
        return False


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard():
    drawBoard = []

    #Loop through positions 1 to 9
    for i in range(1, 10):
        #Check if the position on the game board is empty
        if board[i] == ' ':
            #If it's empty, add the position number as a string
            drawBoard.append(str(i))
        else:
            #If it's not empty, add the 'X' or 'O' from the game board
            drawBoard.append(board[i])

    #Print the board with current marks
    print(f"{drawBoard[0]} | {drawBoard[1]} | {drawBoard[2]}")
    print("---------")
    print(f"{drawBoard[3]} | {drawBoard[4]} | {drawBoard[5]}")
    print("---------")
    print(f"{drawBoard[6]} | {drawBoard[7]} | {drawBoard[8]}")



# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    #Check if the input is a digit
    #Convert the input to an integer
    position = int(position)
    
    #Check if the input is a digit
    if not isinstance(position, int):
        return False
    
    #Check if the position is within the valid range (1-9)
    if position < 1 or position > 9:
        return False

    #Check if the position is already occupied
    if board[position] != ' ':
        return False

    #If none of the above conditions are met, the input is valid
    return True

# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]

]

# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    # Check rows, columns, and diagonals for a win
    for combo in winCombinations:
        if board[combo[0]] == player and board[combo[1]] == player and board[combo[2]] == player:
            return True
        
    return False


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    #use for loop to iterate thru all pos in the board
    for pos in board:
        #if there's empty position, return False
        if board[pos] == ' ':
            return False
    #if full, return True
    return True



#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################

gameEnded = False
currentTurnPlayer = 'X'

# entry point of the whole program
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User
while not gameEnded:
    # Ask for user input and validate it
    move = input(currentTurnPlayer + "'s turn, input (choose number between 1 to 9): ")
    
    # Validate the input
    if validateMove(move):
        # Update the board with the current player's mark
        markBoard(int(move), currentTurnPlayer)
        
        # Print the updated board
        printBoard()
        
        # Check for a win
        if checkWin(currentTurnPlayer):
            print(currentTurnPlayer + " wins! Congratulations!")
            gameEnded = True
        # Check for a tie
        elif checkFull():
            print("It's a tie!")
            gameEnded = True
        else:
            # Switch to the other player's turn
            if currentTurnPlayer == 'X':
                currentTurnPlayer = 'O'
            else:
                currentTurnPlayer = 'X'
    else:
        print("Invalid move. Please try again.")

# Bonus Point: Implement the feature to restart the game
restart = input("Do you want to play again? (yes/no): ")
if restart.lower() == 'yes':
    # Reset the game board
    for pos in board:
        board[pos] = ' '
    gameEnded = False
    currentTurnPlayer = 'X'
    print("\nNew game started!")

