def solution(cap, n, deliveries, pickups):
    total_distance = 0

    delivery_idx = n - 1
    pickup_idx = n - 1

    while delivery_idx >= 0 or pickup_idx >= 0:
        # Find the furthest house needing delivery
        while delivery_idx >= 0 and deliveries[delivery_idx] == 0:
            delivery_idx -= 1
        
        # Find the furthest house needing pickup
        while pickup_idx >= 0 and pickups[pickup_idx] == 0:
            pickup_idx -= 1
        
        if delivery_idx < 0 and pickup_idx < 0:
            break  # All tasks are done

        # Farthest point we must visit this round trip
        farthest = max(delivery_idx, pickup_idx)
        total_distance += (farthest + 1) * 2

        # Deliver packages
        load = cap
        while delivery_idx >= 0 and load > 0:
            if deliveries[delivery_idx] <= load:
                load -= deliveries[delivery_idx]
                deliveries[delivery_idx] = 0
                delivery_idx -= 1
            else:
                deliveries[delivery_idx] -= load
                load = 0

        # Pick up packages
        load = cap
        while pickup_idx >= 0 and load > 0:
            if pickups[pickup_idx] <= load:
                load -= pickups[pickup_idx]
                pickups[pickup_idx] = 0
                pickup_idx -= 1
            else:
                pickups[pickup_idx] -= load
                load = 0

    return total_distance

# Test cases
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # Expected output: 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # Expected output: 30