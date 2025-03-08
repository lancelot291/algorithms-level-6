def solution(cards):
    n = len(cards)
    total_score = 0
    for i in range(n):  #first pick
        visited = [0]*n
        visited[i] = 1
        cur = cards[i]-1
        while visited[cur] == 0:
            visited[cur] = 1
            cur = cards[cur]-1
        score_1 = visited.count(1)
        second_list = list(filter(lambda x : visited[x] == 0, [i for i in range(n)]))

        score_2 = 0 
        if score_1 == n:
            score_2 = 0
        else:
            for j in second_list:
                visited_2 = visited.copy()
                visited_2[j] = 1
                curr = cards[j]-1
                while visited_2[curr] == 0:
                    visited_2[curr] = 1
                    curr = cards[curr]-1
                score_2 = max(visited_2.count(1) - visited.count(1), score_2)

        total_score = max(score_1 * score_2, total_score)

    return total_score

#Test cases
cards = [8,6,3,7,2,5,1,4]
print(solution(cards)) #Expected output: 12


            



    
    