from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(edges) + 1

        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque([(1, 0)])  # (node, depth)
        visited = [False] * (n + 1)
        visited[1] = True

        max_depth = 0

        while q:
            node, depth = q.popleft()
            max_depth = max(max_depth, depth)

            for nei in g[node]:
                if not visited[nei]:
                    visited[nei] = True
                    q.append((nei, depth + 1))

        return pow(2, max_depth - 1, MOD)
