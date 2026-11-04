
from typing import List

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def kth(self, k):
        idx = 0
        bit_mask = 1 << (self.n.bit_length() - 1)

        while bit_mask:
            nxt = idx + bit_mask
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            bit_mask >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        count_tree = Fenwick(m)
        sum_tree = Fenwick(m)

        total = 0

        def add(v, delta):
            nonlocal total
            r = rank[v]
            count_tree.update(r, delta)
            sum_tree.update(r, v * delta)
            total += v * delta

        # Initialize first window
        for i in range(x):
            add(nums[i], 1)

        costs = []

        def get_cost():
            median_idx = count_tree.kth((x + 1) // 2)
            median = vals[median_idx - 1]

            left_count = count_tree.query(median_idx - 1)
            left_sum = sum_tree.query(median_idx - 1)

            through_count = count_tree.query(median_idx)
            through_sum = sum_tree.query(median_idx)

            right_count = x - through_count
            right_sum = total - through_sum

            return (
                median * left_count - left_sum
                + right_sum - median * right_count
            )

        costs.append(get_cost())

        # Calculate costs of all sliding windows
        for i in range(x, n):
            add(nums[i - x], -1)
            add(nums[i], 1)
            costs.append(get_cost())

        # DP
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
