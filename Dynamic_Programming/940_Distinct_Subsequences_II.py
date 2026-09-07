class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp = number of distinct subsequences
        # including the empty subsequence
        dp = 1

        # last[i] stores the dp value before the
        # previous occurrence of character i
        last = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')

            # Double the existing subsequences by either
            # keeping or adding the current character.
            # Subtract duplicates caused by a previous
            # occurrence of the same character.
            new_dp = (2 * dp - last[idx]) % MOD

            last[idx] = dp
            dp = new_dp

        # Remove the empty subsequence
        return (dp - 1) % MOD
