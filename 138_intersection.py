def solution(line):
    n = len(line)
    intersection = []
    
    for i in range(n):
        for j in range(i + 1, n):
            a, b, c = line[i]
            p, q, r = line[j]
            
            if a * q - p * b == 0:  # Check for parallel lines
                continue
            
            #coordinates of intersection point
            x= (b * r - q * c) / (a * q - p * b) 
            y = (c * p - a * r) / (a * q - p * b)
            
            # Check if intersection point is an integer point
            if x.is_integer() and y.is_integer():
                # Append the intersection point as a tuple of integers
                if (int(x), int(y)) not in intersection:
                    intersection.append((int(x), int(y)))
                    
    intersection.sort(key=lambda x: x[0])  # Sort by x-coordinate
    x_min = intersection[0][0]
    x_max = intersection[-1][0]
    col = x_max - x_min + 1  # Number of columns
    
    intersection.sort(key=lambda x: x[1])  # Sort by y-coordinate
    y_min = intersection[0][1]
    y_max = intersection[-1][1]
    row = y_max - y_min + 1  # Number of rows
    
    # Create a grid initialized with dots
    grid = ["." * col for _ in range(row)]
    
    #adjust the coordinates of intersection points
    for i in range(len(intersection)):
        intersection[i] = (intersection[i][0] - x_min, -(intersection[i][1] - y_max))
        
    # Fill the grid with intersection points
    for x, y in intersection:
        grid[y] = grid[y][:x] + "*" + grid[y][x + 1:]

    
    #print(intersection)
    return grid
        
                    
                    
    
# Test cases
line = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
print(solution(line))
            
            