class Solution:
    def containsCycle(self, grid):
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(x, y, px, py, ch):
            if visited[x][y]:
                return True

            visited[x][y] = True

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == ch:
                    if nx == px and ny == py:
                        continue

                    if dfs(nx, ny, x, y, ch):
                        return True

            return False

        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1, grid[i][j]):
                        return True

        return False
