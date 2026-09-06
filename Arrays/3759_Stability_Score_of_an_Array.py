class Solution:
    def firstStableIndex(self, nums, k):
        n = len(nums)

        # suffix_min[i] = minimum value from i to n-1
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # Find the first stable index
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i

        return -1
