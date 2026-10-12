
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bits = [0] * 31

        for num in nums:
            for b in range(31):
                if num & (1 << b):
                    bits[b] += 1

        ans = 0

        for _ in range(k):
            x = 0

            for b in range(31):
                if bits[b] > 0:
                    x |= (1 << b)
                    bits[b] -= 1

            ans = (ans + x * x) % MOD

        return ans
