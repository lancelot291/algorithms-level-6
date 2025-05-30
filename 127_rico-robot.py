from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                start = (i, j)
            elif board[i][j] == "G":
                end = (i, j)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    def move(direction, x, y):
        dx, dy = direction
        while 0 <= x + dx < row and 0 <= y + dy < col and board[x + dx][y + dy] != "D":
            x = x + dx
            y = y + dy
        return (x, y)
    x, y = start
    queue = deque([(x, y, 0)]) 
    visited = set()
    visited.add((x, y))
    while queue:
        x, y, c = queue.popleft()
        if (x, y) == end:
            return c
        for direction in directions:
            nx, ny = move(direction, x, y)
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != "D" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, c + 1))
                
    return -1
        
#Test cases
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board)) #Output: 6

    
