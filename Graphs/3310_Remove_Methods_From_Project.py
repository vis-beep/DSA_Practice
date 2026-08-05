from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods (reachable from k)
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True

        while q:
            node = q.popleft()
            for nei in graph[node]:
                if not suspicious[nei]:
                    suspicious[nei] = True
                    q.append(nei)

        # Check if any non-suspicious method invokes a suspicious method
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        # Return all remaining methods
        return [i for i in range(n) if not suspicious[i]]
