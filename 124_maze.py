from collections import deque
def bfs(start, target, maps):
    """ Performs BFS to find the shortest path between two points in the maze """
    rows, cols = len(maps), len(maps[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set([start])

    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == target:  # If we reach the target
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                if maps[nr][nc] != 'X':  # Only move if it's not a wall
                    queue.append((nr, nc, dist + 1))
                    visited.add((nr, nc))

    return -1  # If no path exists
def solution(maps):
    target_1 = (0, 0)
    target_2 = (0, 0)
    rows, cols = len(maps), len(maps[0])
    for i in range(rows):
        for j in range(cols):
            if maps[i][j] == 'L':
                target_1 = (i, j)
            if maps[i][j] == 'E':
                target_2 = (i, j)
            if maps[i][j] == 'S':
                start = (i, j)
    dist_1 = bfs(start, target_1, maps)
    dist_2 = bfs(target_1, target_2, maps)
    return dist_1 + dist_2 if dist_1 != -1 and dist_2 != -1 else -1

# Test cases
maps = ["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]
print(solution(maps))

