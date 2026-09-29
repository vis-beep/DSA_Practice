class Solution:
    def hasValidPath(self, grid: List[List[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Length of path must be even
        if (m + n - 1) % 2 == 1:
            return False

        # First must be '(' and last must be ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        # dp[i][j] = set of possible balances at (i, j)
        dp = [[set() for _ in range(n)] for _ in range(m)]

        # Starting '(' gives balance 1
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                change = 1 if grid[i][j] == '(' else -1

                # From top
                if i > 0:
                    for balance in dp[i - 1][j]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

                # From left
                if j > 0:
                    for balance in dp[i][j - 1]:
                        new_balance = balance + change

                        if new_balance >= 0:
                            dp[i][j].add(new_balance)

        # Valid path must end with balance 0
        return 0 in dp[m - 1][n - 1]
        
