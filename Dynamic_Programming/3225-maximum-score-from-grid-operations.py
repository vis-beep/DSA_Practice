from typing import List

class Solution:
    def maximumScore(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Build column prefix sums
        prefix = [[0] * n for _ in range(n)]

        for j in range(n):
            prefix[j][0] = grid[0][j]
            for i in range(1, n):
                prefix[j][i] = prefix[j][i - 1] + grid[i][j]

        def col_sum(j: int, lo: int, hi: int) -> int:
            """Sum of column j from row lo to hi (inclusive)."""
            if lo > hi:
                return 0

            result = prefix[j][hi]
            if lo > 0:
                result -= prefix[j][lo - 1]

            return result

        def boundary_score(j: int, h1: int, h2: int) -> int:
            """
            Score from boundary between column j and j+1.
            h1, h2 in range [-1, n-1]
            -1 means column not colored
            """
            if h1 == h2:
                return 0

            if h1 < h2:
                # White cells in col j
                # rows h1+1 to h2
                return col_sum(j, h1 + 1, h2)
            else:
                # White cells in col j+1
                # rows h2+1 to h1
                return col_sum(j + 1, h2 + 1, h1)

        # Heights encoded as:
        # index 0 = height -1
        # index k = height k-1
        dp = [0] * (n + 1)

        for j in range(n - 1):
            new_dp = [-1] * (n + 1)

            for h2 in range(n + 1):
                actual_h2 = h2 - 1
                best = -1

                for h1 in range(n + 1):
                    actual_h1 = h1 - 1

                    val = dp[h1] + boundary_score(
                        j,
                        actual_h1,
                        actual_h2
                    )

                    best = max(best, val)

                new_dp[h2] = best

            dp = new_dp

        return max(dp)
