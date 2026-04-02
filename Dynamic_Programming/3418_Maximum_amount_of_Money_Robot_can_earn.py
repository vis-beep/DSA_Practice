class Solution:
    def maximumAmount(self, coins):
        m, n = len(coins), len(coins[0])
        
        # dp[j][k] = max coins at column j with k neutralizations used
        dp = [[-float('inf')] * 3 for _ in range(n)]
        
        # Initialize start cell (0,0)
        if coins[0][0] >= 0:
            dp[0][0] = coins[0][0]
        else:
            dp[0][0] = coins[0][0]
            dp[0][1] = 0
        
        # First row
        for j in range(1, n):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            for k in range(3):
                if dp[j-1][k] == -float('inf'):
                    continue
                
                val = coins[0][j]
                
                if val >= 0:
                    new_dp[j][k] = max(new_dp[j][k], dp[j-1][k] + val)
                else:
                    new_dp[j][k] = max(new_dp[j][k], dp[j-1][k] + val)
                    if k < 2:
                        new_dp[j][k+1] = max(new_dp[j][k+1], dp[j-1][k])
            
            for k in range(3):
                dp[j][k] = new_dp[j][k]
        
        # Remaining rows
        for i in range(1, m):
            new_dp = [[-float('inf')] * 3 for _ in range(n)]
            
            for j in range(n):
                for k in range(3):
                    val = coins[i][j]
                    
                    # From top
                    if dp[j][k] != -float('inf'):
                        if val >= 0:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k] + val)
                        else:
                            new_dp[j][k] = max(new_dp[j][k], dp[j][k] + val)
                            if k < 2:
                                new_dp[j][k+1] = max(new_dp[j][k+1], dp[j][k])
                    
                    # From left
                    if j > 0 and new_dp[j-1][k] != -float('inf'):
                        if val >= 0:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + val)
                        else:
                            new_dp[j][k] = max(new_dp[j][k], new_dp[j-1][k] + val)
                            if k < 2:
                                new_dp[j][k+1] = max(new_dp[j][k+1], new_dp[j-1][k])
            
            dp = new_dp
        
        return max(dp[n-1])
