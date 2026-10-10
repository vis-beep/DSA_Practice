
class Solution:
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        left, right = 0, max(diff)

        while left < right:
            mid = (left + right) // 2
            needed = sum(max(0, d - mid) for d in diff)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        remaining_ops = k - sum(max(0, d - level) for d in diff)

        ans = 0
        for d in diff:
            reduced = min(d, level)
            ans += reduced * reduced

        return ans - remaining_ops * (2 * level - 1)
