class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        
        # dp[c][0] represents paths moving right into column c
        # dp[c][1] represents paths moving down into column c
        dp = [[0, 0] for _ in range(n + 1)]
        
        # Base setup for the start
        dp[1] = [1, 1]
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    # Mirror: right-moving becomes down-moving, down-moving becomes right-moving
                    dp[c + 1] = [dp[c + 1][1], dp[c][0]]
                else:
                    # Empty cell: can receive from both directions
                    val = (dp[c + 1][1] + dp[c][0]) % MOD
                    dp[c + 1] = [val, val]
                    
        return dp[n][0]
