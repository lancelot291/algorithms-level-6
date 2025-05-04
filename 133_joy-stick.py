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
    visited.add(curr)
    
    while queue:    
        curr_str, index, moves = queue.pop(0)
        
        # Check if we have reached the target string
        if curr_str == name:
            answer = moves
            break
        
        # Calculate the next character to change
        next_char = name[index]
        
        # Calculate the moves needed to change the current character to the target character
        move_count = min_moves(curr_str[index], next_char)
        
        # Create a new string with the updated character
        new_str = curr_str[:index] + next_char + curr_str[index+1:]
        
        # If we haven't visited this string before, add it to the queue
        if new_str not in visited:
            visited.add(new_str)
            queue.append((new_str, (index + 1)%n, moves + move_count+1))
            queue.append((new_str, ((index - 1)+n)%n, moves + move_count+1))
        
        # Move to the next index (right or left)
        next_index = (index + 1) % n
        if next_index not in visited:
            visited.add(curr_str)
            queue.append((curr_str, next_index, moves + 1))
            
    return answer-1
    
        
    
    











#Test case
print(solution("JAZ"))  # Expected output: 11
print(solution("JEROEN"))  # Expected output: 56