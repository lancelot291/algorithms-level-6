def solution(name):
    def min_moves(alpha, target):
        # Calculate the minimum moves to change the current character to the target character
        return min(abs(ord(alpha) - ord(target)), 26 - abs(ord(alpha) - ord(target)))
    n = len(name)
    answer = 0
    curr = 'A'*n
    lst = []
    
    queue = [(curr, 0, 0)]  # (current string, index, moves)
    visited = set()
    visited.add((curr, 0)) # (word, index)
    
    while queue:    
        curr_str, index, moves = queue.pop(0)
        
        # Check if we have reached the target string
        if curr_str == name:
            answer = moves + move_count
            break
        
        # Calculate the next character to change
        next_char = name[index]
        
        # Calculate the moves needed to change the current character to the target character
        move_count = min_moves(curr_str[index], next_char)
        
        # Create a new string with the updated character
        new_str = curr_str[:index] + next_char + curr_str[index+1:]
        
        next_index = (index + 1) % n
        if (new_str, next_index) not in visited:
            visited.add((new_str, next_index))
            queue.append((new_str, (index + 1)%n, moves + move_count+1))
        
        prev_index = (index - 1 + n) % n
        if (new_str, prev_index) not in visited:
            visited.add((new_str, prev_index))
            queue.append((new_str, ((index - 1)+n)%n, moves + move_count+1))
            
    return answer
    
        
    
    











#Test case
print(solution("JAZ"))  # Expected output: 11
print(solution("JEROEN"))  # Expected output: 56