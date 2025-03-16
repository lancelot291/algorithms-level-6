from collections import deque

def solution(board):
    cnt = 0
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
        while 0 <= x + dx < row and 0 <= y + dy < col and board[x][y] != "D":
            nx = x + dx
            ny = y + dy
        return (nx, ny)
    x, y = start
    queue = deque([(x, y, cnt)]) 
    visited = set()
    visited.add((x, y))
    while queue:
        x, y, cnt = queue.popleft()
        if (x, y) == end:
            return cnt
        for dx, dy in directions:
            nx, ny = move((dx, dy), x, y)
            if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != "D" and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, cnt + 1))
        
#Test cases
board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
print(solution(board)) #Output: 6

    
