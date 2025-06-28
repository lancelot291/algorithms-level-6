def solution(cap, n, deliveries, pickups):
    total_distance = 0

    while True:
        # 가장 마지막 배달 지점 찾기
        last_delivery = -1
        for i in range(n - 1, -1, -1):
            if deliveries[i] > 0:
                last_delivery = i
                break

        # 가장 마지막 수거 지점 찾기
        last_pickup = -1
        for i in range(n - 1, -1, -1):
            if pickups[i] > 0:
                last_pickup = i
                break

        # 배달과 수거 모두 완료되었으면 종료
        if last_delivery == -1 and last_pickup == -1:
            break

        # 가장 멀리 있는 지점까지 거리 계산
        last_end = max(last_delivery, last_pickup)
        total_distance += (last_end + 1) * 2

        # 배달 수행
        current_boxes = cap
        i = last_delivery
        while current_boxes > 0 and i >= 0:
            if deliveries[i] > 0:
                if current_boxes >= deliveries[i]:
                    current_boxes -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= current_boxes
                    current_boxes = 0
            i -= 1

        # 수거 수행
        current_boxes = 0
        i = last_pickup
        while current_boxes < cap and i >= 0:
            if pickups[i] > 0:
                if current_boxes + pickups[i] <= cap:
                    current_boxes += pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= (cap - current_boxes)
                    current_boxes = cap
            i -= 1

    return total_distance
# Test cases
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))  # Expected output: 16
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))  # Expected output: 30