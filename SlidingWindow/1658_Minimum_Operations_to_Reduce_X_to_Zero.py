class Solution:
    def minOperations(self, nums, x):
        total = sum(nums)
        target = total - x
        n = len(nums)

        # If we need to keep an empty subarray
        if target == 0:
            return n

        # If target is impossible
        if target < 0:
            return -1

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(n):
            curr_sum += nums[right]

            # Reduce window until sum <= target
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            # Found a subarray with sum == target
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        if max_len == -1:
            return -1

        return n - max_len
