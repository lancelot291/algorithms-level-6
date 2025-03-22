from collections import deque

def solution(board):
    row = len(board)
    col = len(board[0])

    # Find start and goal
    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                start = (i, j)
            elif board[i][j] == "G":
                end = (i, j)

    # Directions: Right, Left, Down, Up
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def move(direction, x, y):
        dx, dy = direction
        while True:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < row and 0 <= ny < col):
                break
            if board[nx][ny] == "D":
                break
            x, y = nx, ny
        return (x, y)

    queue = deque([(start[0], start[1], 0)])  # (x, y, move count)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, count = queue.popleft()
        if (x, y) == end:
            return count
        for direction in directions:
            nx, ny = move(direction, x, y)
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, count + 1))

    return -1  # If goal not reachable