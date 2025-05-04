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
                
    if x < o or x > o + 1:
        return 0
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '.':
            if board[i][0] == 'X' and x != o:
                return 0
            elif board[i][0] == 'O' and x != o-1:
                return 0
        
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '.':
            if board[0][i] == 'X' and x != o:
                return 0
            elif board[0][i] == 'O' and x != o-1:
                return 0
            
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '.':
        if board[0][0] == 'X' and x != o:
            return 0
        elif board[0][0] == 'O' and x != o-1:
            return 0
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '.':
        if board[0][2] == 'X' and x != o:
            return 0
        elif board[0][2] == 'O' and x != o-1:
            return 0
        
    return 1

# Test cases   
print(solution(["O.X", ".O.", "..X"]))  # Expected output: 1
print(solution(["OOO", "...", "XXX"]) ) # Expected output: 0
