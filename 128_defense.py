import heapq
def solution(n, k, enemy):
    max_heap = []
    total_soldiers_used = 0
    
    for round, enemies in enumerate(enemy):
        heapq.heappush(max_heap, -enemies)
        #print(max_heap)
        total_soldiers_used += enemies
        
        if total_soldiers_used > n:
            if k > 0:
                total_soldiers_used += heapq.heappop(max_heap)
                k -= 1
            else:
                return round
        
    return len(enemy)
        
    
    

            
#Test cases
enemy = [4, 2, 4, 5, 3, 3, 1]
n = 7
k = 3
print(solution(n, k, enemy)) #Output: 3
    