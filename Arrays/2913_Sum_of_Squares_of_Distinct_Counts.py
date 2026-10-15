
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0

        for i in range(n):
            distinct = set()

            for j in range(i, n):
                distinct.add(nums[j])
                total += len(distinct) ** 2

        return total
