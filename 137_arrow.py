def solution(n, info):
    # Initialize the maximum score difference and the best answer
    max_diff = 0
    best_answer = [-1]
    
    def dfs(index, arrows_left, ryan_distribution):
        nonlocal max_diff, best_answer
        
        #base case: went through all scores or ran out of arrows
        if index == 11 or arrows_left == 0:
            
            if index == 11 and arrows_left > 0:
                ryan_distribution[10] += arrows_left
            
            # Calculate scores for Ryan and Apeach
            ryan_score = 0
            apeach_score = 0
            for i in range(11):
                if info[i] == 0 and ryan_distribution[i] == 0:
                    continue
                elif ryan_distribution[i] > info[i]:
                    ryan_score += 10 - i
                elif info[i] >= ryan_distribution[i]:
                    apeach_score += 10 - i
                    
            # Check if Ryan's score is better
            if ryan_score > apeach_score:
                diff = ryan_score - apeach_score
                if diff > max_diff or (diff == max_diff and better_dist(ryan_distribution, best_answer)):
                    max_diff = diff
                    best_answer = ryan_distribution[:]
                    
            return
        
        #Ryan wins this round
        required_arrows = info[index] + 1
        if arrows_left >= required_arrows:
            ryan_distribution[index] = required_arrows
            dfs(index + 1, arrows_left - required_arrows, ryan_distribution)
            ryan_distribution[index] = 0
            
        #Ryan loses this round
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
print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))  # Expected output: [0,2,2,0,1,0,0,0,0,0,0]
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))  # Expected output: [-1]
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))  # Expected output: [1,1,2,0,1,2,2,0,0,0,0]
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3])) # Expected output: [1,1,1,1,1,1,1,1,0,0,2]
        
        
                        
            
            
