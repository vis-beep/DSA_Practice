class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = maximum number of valid substrings
        # using the first i characters
        dp = [0] * (n + 1)

        # palindrome[i][j] = True if s[i:j+1] is a palindrome
        palindrome = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or palindrome[i + 1][j - 1]):
                    palindrome[i][j] = True

        for i in range(1, n + 1):
            # Skip the current character
            dp[i] = dp[i - 1]

            # Try every valid palindrome ending at i - 1
            for start in range(i):
                if i - start >= k and palindrome[start][i - 1]:
                    dp[i] = max(dp[i], dp[start] + 1)

        return dp[n]
