

class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)

        # Difference array
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            pair_sum = a + b

            # Initially assume 2 moves for all sums
            diff[2] += 2

            # 1 move range
            diff[low] -= 1
            diff[high + 1] += 1

            # 0 move at exact sum
            diff[pair_sum] -= 1
            diff[pair_sum + 1] += 1

        ans = float('inf')
        current = 0

        # Calculate minimum moves using prefix sum
        for s in range(2, 2 * limit + 1):
            current += diff[s]
            ans = min(ans, current)

        return ans
