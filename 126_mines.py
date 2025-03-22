def solution(picks, minerals):
    # Fatigue table: [diamond pickaxe, iron pickaxe, stone pickaxe]
    fatigue_table = {
        "diamond": [1, 5, 25],
        "iron": [1, 1, 5],
        "stone": [1, 1, 1]
    }

    # Total number of pickaxes available
    total_picks = sum(picks)

    # Step 1: Divide minerals into groups of 5
    mineral_groups = []
    for i in range(0, len(minerals), 5):
        mineral_groups.append(minerals[i:i+5])
        
    if len(mineral_groups) > total_picks:
        mineral_groups = mineral_groups[:total_picks]
        
    def group_value(group):
        return (group.count("diamond"), group.count("iron"), group.count("stone"))
    
    mineral_groups.sort(key=group_value, reverse=True)      
    print(mineral_groups)
    
    
    total_fatigue = 0
    
    while sum(picks) > 0 and mineral_groups:
        pick_type = None
        if picks[0] > 0:
            pick_type = "diamond"
            picks[0] -= 1
        elif picks[1] > 0:
            pick_type = "iron"
            picks[1] -= 1
        elif picks[2] > 0:
            pick_type = "stone"
            picks[2] -= 1
            
        group = mineral_groups.pop(0)
        
        
        for mineral in group:
            total_fatigue += fatigue_table[mineral][["diamond", "iron", "stone"].index(pick_type)]
        
    return total_fatigue

#Test cases
picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks, minerals)) #Output: 13
        
        
        
    
    
    
    
    