board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
     # Given a board and a player’s letter, this function returns True if that player has won.
    return (bo[7] == le and bo[8] == bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[6] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run: # Keep looping until we get a valid move
        move = input('Please select a position to place a \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:  # makes sure we type in a number between 1-9
                if spaceIsFree(move): # check if the move we choose is valid (no other letter is there already)
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

def compMove():
    # Create a list of possible moves
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    # Check for possible winning move to take or to block opponents winning move
    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let): 
                move = i
                return move
    
    # Try to take one of the corners
    cornersOpen = []
    for i in possibleMoves:
        for i in [1,3,7,9]:
            cornersOpen.append(i)
    
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # Try to take the center
    if 5 in possibleMoves:
        move = 5
        return move

    # Try any edge
    edgesOpen = []
    for i in possibleMoves:
        for i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move
 
def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break
        
        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print ('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

        if isBoardFull(board):
            print('Tie Game!')

main()
