def solution(n, l, r):
    bit = [1]
    for _ in range(n):
        for i in range(len(bit)):
            if bit[i] == 1:
                bit = bit[:i] + [1, 1, 0, 1, 1] + bit[i + 1:]
            else:
                bit = bit[:i] + [0, 0, 0, 0, 0] + bit[i + 1:]
                
    bit = bit[l:r+1]
    return sum(bit)

# Test cases
print(solution(2, 4, 17))  # Expected output: 3
    