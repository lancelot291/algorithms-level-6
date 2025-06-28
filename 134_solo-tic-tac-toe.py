def solution(board):
    
    # Count the number of 'X's and 'O's on the board
    x = 0
    o = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                x+=1
            elif board[i][j] == 'O':
                o+=1
                
    #check if the numbers of 'X's and 'O's are valid            
    if x!= o and x != o-1:
        return 0
    
    for i in range(3):
        #horizontal checks
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            if board[i][0] == 'X' and x != o:
                return 0
            elif board[i][0] == 'O' and x != o-1:
                return 0
        
        #vertical checks
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            if board[0][i] == 'X' and x != o:
                return 0
            elif board[0][i] == 'O' and x != o-1:
                return 0
    
    # Check main diagonal        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        if board[0][0] == 'X' and x != o:
            return 0
        elif board[0][0] == 'O' and x != o-1:
            return 0
    
    # Check other diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        if board[0][2] == 'X' and x != o:
            return 0
        elif board[0][2] == 'O' and x != o-1:
            return 0
    
    # If all checks pass, the board is valid    
    return 1


def solution_2(board):
    # Count how many O's and X's are in the board
    o_count = 0
    x_count = 0

    for row in board:
        for cell in row:
            if cell == 'O':
                o_count += 1
            elif cell == 'X':
                x_count += 1

    # Rule 1: O should always be equal to X or X should be just one less than O
    if not (o_count == x_count or o_count == x_count + 1):
        return 0  # Invalid turn sequence

    # Function to check if a player has won
    def is_winner(player):
        # Check rows
        for i in range(3):
            if board[i][0] == player and board[i][1] == player and board[i][2] == player:
                return True  # Row win
        
        # Check columns
        for j in range(3):
            if board[0][j] == player and board[1][j] == player and board[2][j] == player:
                return True  # Column win
        
        # Check main diagonal
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True  # Main diagonal win
        
        # Check other diagonal
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True  # Other diagonal win

        return False  # No win found

    # Check if someone has won
    o_wins = is_winner('O')
    x_wins = is_winner('X')

    # Rule 2: If X has won, then O should have played exactly as many times as X
    if x_wins and o_count != x_count:
        return 0  # X can't win unless O and X played equally

    # Rule 3: If O has won, then O should have played one more time than X
    if o_wins and o_count != x_count + 1:
        return 0  # O can't win unless it played exactly one more turn

    # If all rules are followed, it's a valid board
    return 1

# Test cases   
print(solution(["O.X", ".O.", "..X"]))  # 1 (Valid)
print(solution(["OOO", "...", "XXX"]))  # 0 (Invalid, both can't win)
print(solution(["...", ".X.", "..."]))  # 0 (Invalid, no O to start)
print(solution(["...", "...", "..."]))  # 1 (Valid, empty board)

print(solution(["O.X", ".O.", "..X"]))  # Expected output: 1
print(solution(["OOO", "...", "XXX"]) ) # Expected output: 0
