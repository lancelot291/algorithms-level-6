def solution(n, info):
    best_diff = 0
    best_distribution = [-1]

    # Iterate through all possible combinations using bit masking (2^11 possible cases)
    for mask in range(1, 1 << 11):
        arrows_needed = 0
        ryan_distribution = [0] * 11

        # Calculate how many arrows Ryan needs for each combination
        for i in range(11):
            if mask & (1 << i):  # If bit at position i is set, Ryan attempts to win this region
                arrows_needed += info[i] + 1
                ryan_distribution[i] = info[i] + 1

        # Skip if total arrows needed exceed what Ryan has
        if arrows_needed > n:
            continue

        # Place remaining arrows at the lowest scoring region (0-point)
        ryan_distribution[10] += n - arrows_needed

        # Calculate scores for Ryan and Apeach
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan_distribution[i] == 0:
                continue
            if ryan_distribution[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i

        # Check if Ryan's score is better
        if ryan_score > apeach_score:
            diff = ryan_score - apeach_score

            # Tie-breaker: more arrows on lower points
            if diff > best_diff or (diff == best_diff and better_lower_points(ryan_distribution, best_distribution)):
                best_diff = diff
                best_distribution = ryan_distribution[:]

    return best_distribution

# Helper function for tie-breaking condition
def better_lower_points(dist1, dist2):
    for i in range(10, -1, -1):  # Check from lowest points to highest
        if dist1[i] > dist2[i]:
            return True
        elif dist1[i] < dist2[i]:
            return False
    return False

# Test examples
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # [1,1,1,1,1,1,1,1,0,0,2]