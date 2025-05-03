def solution(name):
    def min_moves(alpha, target):
        # Calculate the minimum moves to change the current character to the target character
        return min(abs(ord(alpha) - ord(target)), 26 - abs(ord(alpha) - ord(target)))
    n = len(name)
    answer = 0
    curr = 'A'*n
    











#Test case
print(solution("JAZ"))  # Expected output: 11
print(solution("JEROEN"))  # Expected output: 56