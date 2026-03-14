# LeetCode 1415
# K-th Lexicographical Happy String

class Solution:
    def getHappyString(self, n, k):
        res = []

        def backtrack(s):
            if len(res) >= k:
                return

            if len(s) == n:
                res.append(s)
                return

            for ch in "abc":
                if not s or s[-1] != ch:
                    backtrack(s + ch)

        backtrack("")

        if k <= len(res):
            return res[k - 1]
        return ""
