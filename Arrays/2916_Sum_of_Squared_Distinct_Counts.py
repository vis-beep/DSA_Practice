
class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, left, right, val):
            length = right - left + 1

            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + length * val * val
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + length * val
            ) % MOD

            lazy[node] = (lazy[node] + val) % MOD

        def push(node, left, right):
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            val = lazy[node]

            apply(node * 2, left, mid, val)
            apply(node * 2 + 1, mid + 1, right, val)

            lazy[node] = 0

        def update(node, left, right, ql, qr, val):
            if ql <= left and right <= qr:
                apply(node, left, right, val)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr, val)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr, val)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last.get(x, -1)

            update(1, 0, n - 1, prev + 1, i, 1)

            last[x] = i
            ans = (ans + tree_sq[1]) % MOD

        return ans
