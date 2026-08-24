#include <limits.h>

long long max(long long a, long long b) {
    return a > b ? a : b;
}

long long stoneGameVIII(int* stones, int stonesSize) {
    int n = stonesSize;

    long long prefix[n];

    // Prefix sums
    prefix[0] = stones[0];

    for (int i = 1; i < n; i++) {
        prefix[i] = prefix[i - 1] + stones[i];
    }

    /*
        dp represents the best score difference
        starting from the current position.

        Initially, if Alice takes all stones:
        score difference = prefix[n - 1]
    */

    long long dp = prefix[n - 1];

    /*
        We can choose a prefix of length i+1.

        Transition:
            dp = max(dp, prefix[i] - dp)

        We process from right to left.
    */

    for (int i = n - 2; i >= 1; i--) {
        dp = max(dp, prefix[i] - dp);
    }

    return dp;
}
