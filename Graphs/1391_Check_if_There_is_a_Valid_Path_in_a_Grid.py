class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # Directions: up, down, left, right
        dirs = {
            1: [(0, -1), (0, 1)],     # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)]      # right, up
        }

        visited = set()

        def is_connected(x, y, nx, ny):
            # Check if next cell connects back to current cell
            for dx, dy in dirs[grid[nx][ny]]:
                if nx + dx == x and ny + dy == y:
                    return True
            return False

        def dfs(x, y):
            if (x, y) == (m - 1, n - 1):
                return True

            visited.add((x, y))

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy

                if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                    if is_connected(x, y, nx, ny):
                        if dfs(nx, ny):
                            return True

            return False

        return dfs(0, 0)
