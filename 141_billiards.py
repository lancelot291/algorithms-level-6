def solution(m, n, startX, startY, balls):
    minimum_distances = []
    # Calculate the minimum distance for each ball
    for endX, endY in balls:
        # Calculate the distance for each possible bounce
        actual_distance = []
        
        # route 1 : bounces off the left wall
        if startY == endY and startX > endX:
            pass
        else:
            actual_distance.append((startX + endX)**2 + (startY - endY)**2)
        
        # route 2 : bounces off the right wall
        if startY == endY and startX < endX:
            pass
        else:
            actual_distance.append((2 * m - startX - endX)**2 + (startY - endY)**2)
        
        # route 3 : bounces off the top wall
        if startX == endX and startY < endY:
            pass
        else:
            actual_distance.append((startX - endX)**2 + (2 * n - startY - endY)**2)
        
        # route 4 : bounces off the bottom wall
        if startX == endX and startY > endY:
            pass
        else:
            actual_distance.append((startX - endX)**2 + (startY + endY)**2)
            
        print(actual_distance)
        
        minimum_distances.append(min(actual_distance))
        

    return minimum_distances

# Test case provided
print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))