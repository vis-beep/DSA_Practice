
class Solution:
    def maxTotal(self, items: list[list[int]], budget: int) -> int:

        n = len(items)

        minPrice = min(price for factor, price in items)

        # Step 1: Calculate value of each item
        values = []

        for i in range(n):
            freeCount = 0

            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    freeCount += 1

            values.append(1 + freeCount)

        # Step 2: 0/1 Knapsack DP
        dp = [0] * (budget + 1)

        for i in range(n):
            factor, price = items[i]
            value = values[i]

            for c in range(budget, price - 1, -1):
                dp[c] = max(
                    dp[c],
                    dp[c - price] + value
                )

        # Step 3: Calculate maximum answer
        ans = 0

        for c in range(budget + 1):
            extra = (budget - c) // minPrice

            ans = max(ans, dp[c] + extra)

        return ans
