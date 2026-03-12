Approach

The problem asks us to maximize the minimum edge strength in the spanning tree.

This can be solved using:

Binary Search on the stability value

Union-Find (Disjoint Set Union)

Greedy selection of edges similar to Kruskal's MST

Steps

Binary search the possible stability value x.

Check feasibility:

Mandatory edges must satisfy strength ≥ x.

Optional edges can be used:

normally if strength ≥ x

upgraded if 2 * strength ≥ x

Use Union-Find to build a spanning tree.

Prefer edges that do not require upgrades.

If a spanning tree with n-1 edges can be formed using ≤ k upgrades, the stability x is feasible.

Time Complexity

Binary Search iterations: log(2 * max_strength)

Union-Find operations per check: O(E α(N))

Overall:

O(E log S)

Where

E = number of edges

S = maximum edge strength

Space Complexity

O(N) for the Union-Find structure.

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


class Solution:
    def maxStability(self, n, edges, k):

        def can(x):
            dsu = DSU(n)
            used = 0
            upgrades = 0

            free = []
            upgrade = []

            for u, v, s, m in edges:
                if m == 1:
                    if s < x:
                        return False
                    if not dsu.union(u, v):
                        return False
                    used += 1
                else:
                    if s >= x:
                        free.append((u, v))
                    elif s * 2 >= x:
                        upgrade.append((u, v))

            for u, v in free:
                if dsu.union(u, v):
                    used += 1

            for u, v in upgrade:
                if used == n - 1:
                    break
                if upgrades == k:
                    break
                if dsu.union(u, v):
                    upgrades += 1
                    used += 1

            return used == n - 1

        lo, hi = 1, max(s for _, _, s, _ in edges) * 2
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans
