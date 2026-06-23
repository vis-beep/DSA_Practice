class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        k = r - l + 1
        
        # dp[j][0] -> ends at j, last step was a decrease (\), next must increase (/)
        # dp[j][1] -> ends at j, last step was an increase (/), next must decrease (\)
        dp = [[0, 0] for _ in range(k)]
        
        # Base case for length 2:
        for j in range(k):
            dp[j][0] = k - 1 - j  # Choices for a strictly greater previous element
            dp[j][1] = j          # Choices for a strictly smaller previous element
            
        # Transition for lengths 3 to n
        for i in range(3, n + 1):
            next_dp = [[0, 0] for _ in range(k)]
            
            # Suffix sum for type 0 transition (next step is a decrease)
            suffix_sum = 0
            for j in range(k - 1, -1, -1):
                next_dp[j][0] = suffix_sum % MOD
                suffix_sum += dp[j][1]
                
            # Prefix sum for type 1 transition (next step is an increase)
            prefix_sum = 0
            for j in range(k):
                next_dp[j][1] = prefix_sum % MOD
                prefix_sum += dp[j][0]
                
            dp = next_dp
            
        # Sum up all valid sequences of length n
        ans = 0
        for j in range(k):
            ans = (ans + dp[j][0] + dp[j][1]) % MOD
            
        return ans
