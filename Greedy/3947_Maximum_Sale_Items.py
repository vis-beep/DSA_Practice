
from bisect import bisect_right


class Solution:
    def maximumSaleItems(self, items: list[list[int]], budget: int) -> int:

        n = len(items)

        # Count frequencies of factors
        freq = [0] * (n + 1)

        for f, p in items:
            freq[f] += 1

        # Calculate free-copy opportunities
        free = [0] * n

        for i, (f, p) in enumerate(items):
            count = 0

            for j in range(f, n + 1, f):
                count += freq[j]

            free[i] = count - 1

        # Create bonus purchase groups
        groups = []
        group_index = [-1] * n

        for i in range(n):
            if free[i] > 0:
                group_index[i] = len(groups)
                groups.append((items[i][1], free[i]))

        groups.sort()

        m = len(groups)

        prices = [g[0] for g in groups]
        counts = [g[1] for g in groups]

        prefix_count = [0] * (m + 1)
        prefix_cost = [0] * (m + 1)

        for i in range(m):
            prefix_count[i + 1] = (
                prefix_count[i] + counts[i]
            )

            prefix_cost[i + 1] = (
                prefix_cost[i] + prices[i] * counts[i]
            )

        # Cost of q cheapest bonus purchases
        # excluding one group if necessary
        def cost_first(q, limit, excluded):

            if q == 0:
                return 0

            left, right = 0, limit

            while left < right:
                mid = (left + right) // 2

                available = prefix_count[mid + 1]

                if 0 <= excluded <= mid:
                    available -= counts[excluded]

                if available >= q:
                    right = mid
                else:
                    left = mid + 1

            k = left

            before_count = prefix_count[k]
            before_cost = prefix_cost[k]

            if 0 <= excluded < k:

                before_count -= counts[excluded]

                before_cost -= (
                    prices[excluded] * counts[excluded]
                )

            remaining = q - before_count

            return (
                before_cost + remaining * prices[k]
            )

        # Binary search for maximum bonus-only purchases
        lo, hi = 0, prefix_count[m]

        while lo < hi:

            mid = (lo + hi + 1) // 2

            if cost_first(
                mid, m - 1, -1
            ) <= budget:
                lo = mid
            else:
                hi = mid - 1

        answer = 2 * lo

        # Try each item type as the unlimited normal purchase
        for i in range(n):

            p = items[i][1]
            d = free[i]

            mandatory = p * d

            if mandatory > budget:
                continue

            remaining = budget - mandatory

            # Bonus purchases costing at most 2*p
            limit = bisect_right(prices, 2 * p) - 1

            excluded = group_index[i]

            available = (
                prefix_count[limit + 1]
                if limit >= 0 else 0
            )

            if 0 <= excluded <= limit:
                available -= counts[excluded]

            # Find maximum affordable bonus purchases
            lo, hi = 0, available

            while lo < hi:

                mid = (lo + hi + 1) // 2

                cost = cost_first(
                    mid, limit, excluded
                )

                if cost <= remaining:
                    lo = mid
                else:
                    hi = mid - 1

            bonus = lo

            used = cost_first(
                bonus, limit, excluded
            )

            # Buy remaining normal copies
            normal = (remaining - used) // p

            total = 2 * d + 2 * bonus + normal

            answer = max(answer, total)

        return answer
