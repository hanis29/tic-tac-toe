#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#

# import libraries
import unittest

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

    # Loop through positions 1 to 9
    for i in range(1, 10):
    # Check if the position on the game board is empty
        if board[i] == ' ':
        # If it's empty, add the position number as a string
            drawBoard.append(str(i))
        else:
        # If it's not empty, add the 'X' or 'O' from the game board
            drawBoard.append(board[i])

    # Print the board with current marks
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
    # Check if the input is a digit
    # Convert the input to an integer
    position = int(position)
    
    # Check if the input is a digit
    if not isinstance(position, int):
        return False
    
    # Check if the position is within the valid range (1-9)
    if position < 1 or position > 9:
        return False

    # Check if the position is already occupied
    if board[position] != ' ':
        return False

    # If none of the above conditions are met, the input is valid
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




# Main Program, a Tester for your functions
# It does not cover the printBoard() function.

tc = unittest.TestCase()

# Test validateMove()
tc.assertEqual(validateMove(0), False, "validateMove() didn't work as expected with input : 0")
tc.assertEqual(validateMove(10), False, "validateMove() didn't work as expected with input : 10")
tc.assertEqual(validateMove('1'), True, "validateMove() didn't work as expected with input : 1")
tc.assertEqual(validateMove('5'), True, "validateMove() didn't work as expected with input : 5")
tc.assertEqual(validateMove('9'), True, "validateMove() didn't work as expected with input : 9")

testBoard = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'O', 5: 'X', 6: 'O',
    7: ' ', 8: ' ', 9: ' '
}

# Test markBoard()
markBoard(1, 'X')
markBoard(2, 'O')
markBoard(3, 'X')
markBoard(4, 'O')
markBoard(5, 'X')
markBoard(6, 'O')

tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected")

tc.assertEqual(validateMove('1'), False, "validateMove() didn't work as expected with duplicated input : 1")

# Test checkWin()
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")
testBoard[7] = 'X'
markBoard(7, 'X')
tc.assertDictEqual(board, testBoard, "markBoard() didn't work as expected with input (7, 'X')")
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")


board = {
    1: 'X', 2: ' ', 3: ' ',
    4: 'O', 5: 'X', 6: ' ',
    7: 'O', 8: ' ', 9: 'X'
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'O', 2: ' ', 3: ' ',
    4: 'X', 5: 'O', 6: ' ',
    7: 'X', 8: 'X', 9: 'O'
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'O', 3: 'O',
    4: 'X', 5: ' ', 6: ' ',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'O', 3: 'X',
    4: 'X', 5: 'O', 6: ' ',
    7: ' ', 8: 'O', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")

board = {
    1: 'X', 2: 'X', 3: 'X',
    4: 'O', 5: 'O', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('X'), True, "checkWin() didn't work as expected with input : 'X'")
tc.assertEqual(checkWin('O'), False, "checkWin() didn't work as expected with input : 'O'")

board = {
    1: 'X', 2: 'X', 3: ' ',
    4: 'O', 5: 'O', 6: 'O',
    7: 'X', 8: ' ', 9: ' '
}
tc.assertEqual(checkWin('O'), True, "checkWin() didn't work as expected with input : 'O'")
tc.assertEqual(checkWin('X'), False, "checkWin() didn't work as expected with input : 'X'")


# Test checkFull()
tc.assertEqual(checkFull(), False, "checkFull() didn't work as expected")
board = {
    1: 'O', 2: 'X', 3: 'O',
    4: 'O', 5: 'X', 6: 'X',
    7: 'X', 8: 'O', 9: 'X'
}
tc.assertEqual(checkFull(), True, "checkFull() didn't work as expected")

print("All tests passed! Congratulations!")