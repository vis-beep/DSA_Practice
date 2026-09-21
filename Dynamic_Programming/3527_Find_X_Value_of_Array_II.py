class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k

            # Start a new subarray
            new_dp[val] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_r = (r * val) % k
                    new_dp[new_r] += dp[r]

            # Add all subarrays ending at current position
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
        
