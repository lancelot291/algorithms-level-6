def solution(picks, minerals):
    # Fatigue table: pickaxe vs mineral
    fatigue_table = {
        "diamond": [1, 1, 1],      # pickaxe: diamond
        "iron":    [5, 1, 1],      # pickaxe: iron
        "stone":   [25, 5, 1]      # pickaxe: stone
    }

    # Total pickaxes available
    total_picks = sum(picks)

    # Step 1: Group minerals into chunks of 5
    mineral_groups = [minerals[i:i+5] for i in range(0, len(minerals), 5)]
    
    # Step 2: Only consider groups up to the number of pickaxes we have
    mineral_groups = mineral_groups[:total_picks]

    # Step 3: Sort groups by importance — prioritize groups with more diamonds/iron
    def group_score(group):
        # Higher scores mean the group should be mined with better pickaxes
        score = 0
        for mineral in group:
            if mineral == "diamond":
                score += 25
            elif mineral == "iron":
                score += 5
            else:
                score += 1
        return score

    mineral_groups.sort(key=group_score, reverse=True)

    # Step 4: Assign best pickaxe to highest-value group
    total_fatigue = 0
    pickaxe_types = ["diamond", "iron", "stone"]

    for group in mineral_groups:
        # Choose the best available pickaxe
        pick_type = None
        for i in range(3):
            if picks[i] > 0:
                pick_type = pickaxe_types[i]
                picks[i] -= 1
                break

        # If no pickaxes are left, stop
        if not pick_type:
            break

        # Step 5: Calculate fatigue for this group with the chosen pickaxe
        for mineral in group:
            idx = ["diamond", "iron", "stone"].index(mineral)
            total_fatigue += fatigue_table[pick_type][idx]

    return total_fatigue

# **Test Cases including Edge Cases**
test_cases = [
    ([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]),  # Expected 12
    ([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]),  # Expected 50
    ([2, 1, 0], ["diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond", "diamond"]),  # Only diamond, Expected 10
    ([0, 0, 1], ["diamond", "diamond", "diamond", "diamond", "diamond"]),  # Only stone pickaxe, Expected 125
    ([1, 0, 0], ["stone", "stone", "stone", "stone", "stone"]),  # Only stone, but diamond pickaxe available, Expected 5
    ([1, 1, 1], ["iron", "iron", "iron", "iron", "iron", "diamond", "diamond", "diamond", "diamond", "diamond"]),  # Mixed, Expected 10
    ([3, 3, 3], ["stone"] * 50),  # All stone, Expected 45
]

# Run tests
results = [solution(picks, minerals) for picks, minerals in test_cases]
results

print(results)  # Expected: [12, 50, 10, 125, 5, 10, 45]