def solution(users, emoticons):
    discount_rate = [10, 20, 30, 40]
    best_result = [0, 0]  # [number of subscribers, total sales]

    # DFS function to evaluate each discount combination
    def dfs(idx, current_discounts):
        nonlocal best_result

        # if all emoticons have discounts set
        if idx == len(emoticons):
            total_sales = 0
            num_users = 0

            # Calculate total sales and number of subscribers
            for user_discount, user_budget in users:
                total_spent = 0

                # Calculate spending per user
                for i in range(len(emoticons)):
                    if current_discounts[i] >= user_discount:
                        total_spent += emoticons[i] * (100 - current_discounts[i]) // 100

                # Check if user subscribes or just buys
                if total_spent >= user_budget:
                    num_users += 1
                else:
                    total_sales += total_spent

            # Update the best result
            if num_users > best_result[0] or (num_users == best_result[0] and total_sales > best_result[1]):
                best_result[0] = num_users
                best_result[1] = total_sales
            return

        # backtracking step: try discounts for each emoticon
        backtrack(idx, current_discounts)

    # Backtrack function to iterate through discount rates
    def backtrack(idx, current_discounts):
        for rate in discount_rate:
            current_discounts.append(rate)
            dfs(idx + 1, current_discounts)
            current_discounts.pop()

    # Begin DFS with empty discounts
    dfs(0, [])

    return best_result


# Test case:
users = [[40, 10000], [25, 10000]]
emoticons = [7000, 9000]
print(solution(users, emoticons))  # Expected output: [1, 5400]
