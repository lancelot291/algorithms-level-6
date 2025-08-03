def solution(grid):
    row, col = len(grid), len(grid[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
    visited = [[[False] * 4 for _ in range(col)] for _ in range(row)]
    cycles = []
    
    for r in range(row):
        for c in range(col):
            for d in range(4):
                if visited[r][c][d]:
                    continue
                
                length = 0
                x, y, direction = r, c, d
                
                while 0 <= x < row and 0 <= y < col and not visited[x][y][direction]:
                    visited[x][y][direction] = True
                    length += 1
                    
                    dx, dy = directions[direction]
                    x, y = (x + dx) % row, (y + dy) %  col
                    
                    if grid[x][y] == 'L':
                        direction = (direction - 1) % 4
                    elif grid[x][y] == 'R':
                        direction = (direction + 1) % 4
                        
                        
                cycles.append(length)
    
    return cycles

# Test case provided
print(solution(["SL", "LR"]))  # Output: [16]
                        
                        