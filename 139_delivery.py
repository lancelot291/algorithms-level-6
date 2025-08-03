def solution(cap, n, deliveries, pickups):
    total_distance = 0
    current_boxes = 0
    
    while sum(deliveries) > 0 or sum(pickups) > 0:
        # Find the last delivery point with boxes
        last_delivery = n - 1
        for i in range(n - 1, -1, -1):
            if deliveries[i] > 0:
                last_delivery = i
                break
        
        # Find the last pickup point with boxes
        last_pickup = n - 1
        for i in range(n - 1, -1, -1):
            if pickups[i] > 0:
                last_pickup = i
                break
            
        last_end = max(last_delivery, last_pickup)
        total_distance += (last_end + 1) * 2  
        
        #from warehouse to last end delivering boxes
        current_boxes = cap
        while current_boxes > 0 and last_delivery >= 0:
            if deliveries[last_delivery] > 0:
                if current_boxes >= deliveries[last_delivery]:
                    current_boxes -= deliveries[last_delivery]
                    deliveries[last_delivery] = 0
                else:
                    deliveries[last_delivery] -= current_boxes
                    current_boxes = 0
                last_delivery -= 1  
            else:
                last_delivery -= 1
        
        #from last end to warehouse picking up boxes
        current_boxes = 0
        while current_boxes < cap and last_pickup >= 0:
            if pickups[last_pickup] > 0:
                if current_boxes + pickups[last_pickup] <= cap:
                    current_boxes += pickups[last_pickup]
                    pickups[last_pickup] = 0
                else:
                    pickups[last_pickup] -= (cap - current_boxes)
                    current_boxes = cap
                last_pickup -= 1
            else:
                last_pickup -= 1
                
        
    return total_distance

# Test cases
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # Expected output: 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # Expected output: 30
                
        
            
        
        
        
    
    