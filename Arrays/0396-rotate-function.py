class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)
        
        # Compute F(0)
        F = sum(i * num for i, num in enumerate(nums))
        max_val = F
        
        # Compute F(1) to F(n-1)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_val = max(max_val, F)
        
        return max_val
