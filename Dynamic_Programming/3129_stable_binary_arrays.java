/*
Problem: Count Stable Binary Arrays

A binary array is stable if:
1. It contains exactly `zero` number of 0s
2. It contains exactly `one` number of 1s
3. No more than `limit` identical elements appear consecutively

Approach:
Dynamic Programming

dp[i][j][0] → ways using i zeros and j ones ending with 0
dp[i][j][1] → ways using i zeros and j ones ending with 1

Transition:
- Append 0 after up to `limit` ones
- Append 1 after up to `limit` zeros

Time Complexity: O(zero * one * limit)
Space Complexity: O(zero * one)
*/

class Solution {

    private static final int MOD = 1000000007;

    public int numberOfStableArrays(int zero, int one, int limit) {

        long[][][] dp = new long[zero + 1][one + 1][2];

        // Base case: arrays containing only zeros
        for (int i = 1; i <= Math.min(limit, zero); i++) {
            dp[i][0][0] = 1;
        }

        // Base case: arrays containing only ones
        for (int j = 1; j <= Math.min(limit, one); j++) {
            dp[0][j][1] = 1;
        }

        for (int i = 0; i <= zero; i++) {
            for (int j = 0; j <= one; j++) {

                // Add zero at the end
                if (i > 0) {
                    for (int k = 1; k <= Math.min(limit, i); k++) {
                        dp[i][j][0] = (dp[i][j][0] + dp[i - k][j][1]) % MOD;
                    }
                }

                // Add one at the end
                if (j > 0) {
                    for (int k = 1; k <= Math.min(limit, j); k++) {
                        dp[i][j][1] = (dp[i][j][1] + dp[i][j - k][0]) % MOD;
                    }
                }
            }
        }

        return (int)((dp[zero][one][0] + dp[zero][one][1]) % MOD);
    }
}
