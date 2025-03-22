def solution(k, ranges):
    dict_point = {}
    dict_point[0] = k
    x = 1
    while k != 1:
        if k % 2 == 0:
            dict_point[x] = k//2
            x += 1
            k = k/2
        else:
            dict_point[x] = 3*k + 1
            x += 1
            k = 3*k + 1
    print(dict_point)
    n = len(dict_point) - 1
    result = []
            
    for interval in ranges:
        sum = 0
        start = interval[0]
        end = n + interval[1]
        if start == end:
            result.append(0.0)
        elif start > end:  
            result.append(-1.0)
        else:
            for i in range(start, end):
                area = (dict_point[i] + dict_point[i+1])/2.0
                sum += area
            result.append(sum)
            
    return result
    
    
    
    
    
#Test cases
k = 5
ranges = [[0,0],[0,-1],[2,-3],[3,-3]]
print(solution(k, ranges)) #Output: {0: 5, 1: 16, 2: 8, 3: 4, 4: 2, 5: 1}
        