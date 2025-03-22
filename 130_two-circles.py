import math

def solution(r1, r2):
    cnt = 0
    for i in range(1, r2+1):
        if i <r1:
            floor = math.ceil(math.sqrt(r1**2 - i**2))
        else:
            floor = 0
            
        ceil = math.floor(math.sqrt(r2**2 - i**2))
        cnt += ceil - floor + 1
    return cnt*4

#Test cases
print(solution(2, 3)) #Output: 5


    