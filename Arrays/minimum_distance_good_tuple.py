"""
Problem: Minimum Distance of a Good Tuple

A tuple (i, j, k) is good if:
nums[i] == nums[j] == nums[k] and i, j, k are distinct.

Distance = |i-j| + |j-k| + |k-i|

Optimized Insight:
For i < j < k:
Distance = 2 * (k - i)

Approach:
1. Store indices of each number
2. For each value, check consecutive triples
3. Minimize 2 * (k - i)

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from collections import defaultdict


class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)

        # Store indices for each number
        for i, val in enumerate(nums):
            pos[val].append(i)

        ans = float('inf')

        # Check triples
        for indices in pos.values():
            if len(indices) < 3:
                continue

            for i in range(len(indices) - 2):
                left = indices[i]
                right = indices[i + 2]

                dist = 2 * (right - left)
                ans = min(ans, dist)

        return ans if ans != float('inf') else -1


# Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumDistance([1, 2, 1, 1, 3]))  # Output: 6
    print(sol.minimumDistance([1, 1, 2, 3, 2, 1, 2]))  # Output: 8
    print(sol.minimumDistance([1]))  # Output: -1
