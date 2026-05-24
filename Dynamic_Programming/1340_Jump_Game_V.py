# 1340. Jump Game V

## Problem
Given an array of integers `arr` and an integer `d`.

In one step you can jump from index `i` to:

- `i + x` where:
  - `i + x < arr.length`
  - `0 < x <= d`

- `i - x` where:
  - `i - x >= 0`
  - `0 < x <= d`

You can jump from index `i` to index `j` only if:

- `arr[i] > arr[j]`
- `arr[i] > arr[k]` for all indices between `i` and `j`

Return the maximum number of indices you can visit.

---

## Approach
Use **DFS + Memoization (DP)**.

For every index:
- Explore left up to distance `d`
- Explore right up to distance `d`
- Stop if a higher or equal element blocks the jump

Store results in DP to avoid recomputation.

---

## Time Complexity
- **O(n × d)**

## Space Complexity
- **O(n)**

---

## Python Solution

```python
class Solution:
    def maxJumps(self, arr, d):
        n = len(arr)
        dp = [-1] * n

        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # Move left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            # Move right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))

            dp[i] = ans
            return ans

        return max(dfs(i) for i in range(n))
