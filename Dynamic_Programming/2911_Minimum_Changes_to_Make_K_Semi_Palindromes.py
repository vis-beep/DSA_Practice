
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute cost for every substring
        cost = [[INF] * n for _ in range(n)]

        for i in range(n):
            for length in range(2, n - i + 1):
                best = INF

                # Try every proper divisor
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Build and check each group
                    for r in range(d):
                        group = []

                        for pos in range(i + r, i + length, d):
                            group.append(s[pos])

                        # Make this group a palindrome
                        left = 0
                        right = len(group) - 1

                        while left < right:
                            if group[left] != group[right]:
                                changes += 1

                            left += 1
                            right -= 1

                    best = min(best, changes)

                cost[i][i + length - 1] = best

        # DP: dp[i][j] = minimum changes to partition
        # first i characters into exactly j parts
        dp = [[INF] * (k + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):

                for p in range(2 * (j - 1), i - 1):

                    if dp[p][j - 1] == INF:
                        continue

                    dp[i][j] = min(
                        dp[i][j],
                        dp[p][j - 1] + cost[p][i - 1]
                    )

        return dp[n][k]
