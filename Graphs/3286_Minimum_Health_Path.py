from heapq import heappush, heappop

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        # Minimum health lost to reach each cell
        dist = [[float('inf')] * n for _ in range(m)]

        start_cost = grid[0][0]
        dist[0][0] = start_cost

        pq = [(start_cost, 0, 0)]

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            cost, x, y = heappop(pq)

            if cost > dist[x][y]:
                continue

            if x == m - 1 and y == n - 1:
                return cost < health

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost + grid[nx][ny]

                    if new_cost < dist[nx][ny]:
                        dist[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))

        return False
