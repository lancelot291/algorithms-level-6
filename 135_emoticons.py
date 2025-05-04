def solution(users, emoticons):
    dict_ratio = {}
    for i in range(len(users)):
        dict_ratio[i+1] = users[i][0]
    dict_limit = {}
    for i in range(len(users)):
        dict_limit[i+1] = users[i][1]
        
    print(dict_ratio)
    print(dict_limit)
        
        
#Test case
users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))  # Expected output: (1, 5400)