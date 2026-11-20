
class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()

        dp = {}
        ans = 0

        for num in nums:
            a = dp.get(num, 0) + 1
            b = dp.get(num + 1, 0) + 1

            dp[num + 1] = max(dp.get(num + 1, 0), a)
            dp[num + 2] = max(dp.get(num + 2, 0), b)

            ans = max(ans, a, b)

        return ans
