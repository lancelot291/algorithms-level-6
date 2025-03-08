def solution(n):
    arr = []
    def hanoi(n, start, end, mid):
        if n==1:
            arr.append([start, end])
            return

        hanoi(n-1, start, mid, end)
        arr.append([start, end])
        hanoi(n-1, mid, end, start)

    hanoi(n, 1, 3, 2)

    return arr

#Test_cases
n = 2
print(solution(2))
