from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        n = len(digits)

        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        pref_val = [0] * (n + 1)
        for i in range(n):
            pref_val[i + 1] = (pref_val[i] * 10 + digits[i]) % MOD

        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        ans = []

        for l, r in queries:
            left = bisect_left(pos, l)
            right = bisect_right(pos, r)

            if left == right:
                ans.append(0)
                continue

            length = right - left

            value = (pref_val[right] - pref_val[left] * pow10[length]) % MOD
            digit_sum = pref_sum[right] - pref_sum[left]

            ans.append((value * digit_sum) % MOD)

        return ans
