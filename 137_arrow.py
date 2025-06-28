def solution(n, info):
    max_diff = 0
    best_answer = [-1]
    
    def dfs(index, arrows_left, ryan_distribution):
        nonlocal max_diff, best_answer
        
        if index == 11 or arrows_left == 0:
            # Always assign leftover arrows if any remain (moved outside index check)
            if arrows_left > 0:
                ryan_distribution[10] += arrows_left
            
            ryan_score = apeach_score = 0
            for i in range(11):
                if info[i] == 0 and ryan_distribution[i] == 0:
                    continue
                elif ryan_distribution[i] > info[i]:
                    ryan_score += 10 - i
                else:
                    apeach_score += 10 - i
                    
            if ryan_score > apeach_score:
                diff = ryan_score - apeach_score
                if diff > max_diff or (diff == max_diff and better_dist(ryan_distribution, best_answer)):
                    max_diff = diff
                    best_answer = ryan_distribution[:]
            
            # Backtrack the assignment of leftover arrows
            if arrows_left > 0:
                ryan_distribution[10] -= arrows_left
                
            return
        
        required_arrows = info[index] + 1
        if arrows_left >= required_arrows:
            ryan_distribution[index] = required_arrows
            dfs(index + 1, arrows_left - required_arrows, ryan_distribution)
            ryan_distribution[index] = 0
            
        dfs(index + 1, arrows_left, ryan_distribution)
        
    def better_dist(dist1, dist2):
        for i in range(10, -1, -1):
            if dist1[i] > dist2[i]:
                return True
            elif dist1[i] < dist2[i]:
                return False
        return False
    
    dfs(0, n, [0] * 11)
    return best_answer if best_answer != [-1] else [-1]

# Test cases
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # [1,1,1,1,1,1,1,1,0,0,2]