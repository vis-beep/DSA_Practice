class Solution:
    def minBitwiseArray(self, nums):
        ans = []

        for p in nums:
            trailing_ones = 0
            x = p

            # Count trailing 1s
            while x & 1:
                trailing_ones += 1
                x >>= 1

            if trailing_ones == 0:
                ans.append(-1)
            else:
                ans.append(p - (1 << (trailing_ones - 1)))

        return ans
