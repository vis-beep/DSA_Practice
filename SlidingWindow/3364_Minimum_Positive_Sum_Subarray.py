
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')
        n = len(nums)

        for i in range(n):
            curr_sum = 0

            for j in range(i, min(n, i + r)):
                curr_sum += nums[j]
                length = j - i + 1

                if l <= length <= r and curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)

        return min_sum if min_sum != float('inf') else -1
