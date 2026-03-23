class Solution:
    def maxProductPath(self, grid):
        """
        Returns the maximum non-negative product from top-left to bottom-right.
        If no such path exists, returns -1.

        Approach:
        - Use DP to track both max and min product at each cell.
        - Negative values can flip min to max and vice versa.
        """
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # DP arrays
        max_dp = [[0] * n for _ in range(m)]
        min_dp = [[0] * n for _ in range(m)]

        # Initialize starting cell
        max_dp[0][0] = grid[0][0]
        min_dp[0][0] = grid[0][0]

        # Fill first column
        for i in range(1, m):
            val = grid[i][0]
            max_dp[i][0] = max_dp[i - 1][0] * val
            min_dp[i][0] = max_dp[i][0]

        # Fill first row
        for j in range(1, n):
            val = grid[0][j]
            max_dp[0][j] = max_dp[0][j - 1] * val
            min_dp[0][j] = max_dp[0][j]

        # Fill rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]

                candidates = (
                    val * max_dp[i - 1][j],
                    val * min_dp[i - 1][j],
                    val * max_dp[i][j - 1],
                    val * min_dp[i][j - 1],
                )

                max_dp[i][j] = max(candidates)
                min_dp[i][j] = min(candidates)

        result = max_dp[m - 1][n - 1]

        return result % MOD if result >= 0 else -1
