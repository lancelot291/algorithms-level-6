def solution(targets):
    # Sort the targets based on their end positions
    targets.sort(key=lambda x: x[1])
    
    # Initialize the count of arrows and the position of the last arrow
    arrows = 0
    last_arrow_position = -1
    
    for start, end in targets:
        # If the start of the current target is greater than the position of the last arrow,
        # we need to shoot a new arrow
        if start >= last_arrow_position:
            arrows += 1
            last_arrow_position = end  # Update the position of the last arrow
    
    return arrows

# Test case
print(solution([[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]))