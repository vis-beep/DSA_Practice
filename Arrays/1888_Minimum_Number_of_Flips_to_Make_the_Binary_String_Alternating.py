Approach:
- Used sliding window with string doubling to simulate rotations.
- Compared with two alternating patterns (0101... and 1010...).
- Tracked mismatches to compute minimum flips.

Time Complexity: O(n)
Space Complexity: O(n)

#Code

class Solution(object):
    def minFlips(self, s):
        n = len(s)
        s = s + s

        alt1 = ""
        alt2 = ""

        for i in range(len(s)):
            if i % 2 == 0:
                alt1 += "0"
                alt2 += "1"
            else:
                alt1 += "1"
                alt2 += "0"

        res = float('inf')
        diff1 = diff2 = 0
        l = 0

        for r in range(len(s)):
            if s[r] != alt1[r]:
                diff1 += 1
            if s[r] != alt2[r]:
                diff2 += 1

            if r - l + 1 > n:
                if s[l] != alt1[l]:
                    diff1 -= 1
                if s[l] != alt2[l]:
                    diff2 -= 1
                l += 1

            if r - l + 1 == n:
                res = min(res, diff1, diff2)

        return res


