
def solution(name):
    def min_moves(alpha, target):
        # Calculate minimum moves vertically (up/down) to reach target alphabet.
        return min(abs(ord(alpha) - ord(target)), 26 - abs(ord(alpha) - ord(target)))

    answer = 0
    n = len(name)

    # Calculate vertical moves for each letter.
    for ch in name:
        answer += min_moves('A', ch)

    # Calculate minimum horizontal cursor moves.
    move = n - 1  # default horizontal moves (move right all the way)

    # Edited: Optimized cursor movement calculation
    for idx in range(n):
        next_idx = idx + 1
        # Find next index of a character that's not 'A'
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # Calculate move if we reverse direction at idx position
        # Edited: Added correct logic to consider reversing direction
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer

# Test case
print(solution("JAZ"))      # Expected output: 11
print(solution("JEROEN"))   # Expected output: 56
print(solution("JAN"))      # Expected output: 23