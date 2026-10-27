class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#'] * n for _ in range(m)]

        # Open the first row
        for j in range(n):
            grid[0][j] = '.'

        # Open the last column
        for i in range(m):
            grid[i][n - 1] = '.'

        return [''.join(row) for row in grid]
