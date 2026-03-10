"""
Problem: Count Stable Binary Arrays

A binary array is called stable if:
1. It contains exactly `zero` number of 0s
2. It contains exactly `one` number of 1s
3. No more than `limit` identical elements appear consecutively

Approach:
Dynamic Programming

dp0[i][j] → number of ways using i zeros and j ones ending with 0
dp1[i][j] → number of ways using i zeros and j ones ending with 1

Time Complexity: O(zero × one)
Space Complexity: O(zero × one)
"""

class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp0 = [[0] * (one + 1) for _ in range(zero + 1)]
        dp1 = [[0] * (one + 1) for _ in range(zero + 1)]

        # Base cases
        for i in range(1, min(zero, limit) + 1):
            dp0[i][0] = 1

        for j in range(1, min(one, limit) + 1):
            dp1[0][j] = 1

        # Fill DP table
        for i in range(1, zero + 1):
            for j in range(1, one + 1):

                # Place 0
                dp0[i][j] = (dp0[i-1][j] + dp1[i-1][j]) % MOD
                if i > limit:
                    dp0[i][j] = (dp0[i][j] - dp1[i-limit-1][j]) % MOD

                # Place 1
                dp1[i][j] = (dp1[i][j-1] + dp0[i][j-1]) % MOD
                if j > limit:
                    dp1[i][j] = (dp1[i][j] - dp0[i][j-limit-1]) % MOD

        return (dp0[zero][one] + dp1[zero][one]) % MOD


# Example Usage
if __name__ == "__main__":
    sol = Solution()

    print(sol.numberOfStableArrays(1, 1, 2))  # Output: 2
    print(sol.numberOfStableArrays(1, 2, 1))  # Output: 1
    print(sol.numberOfStableArrays(3, 3, 2))  # Output: 14
