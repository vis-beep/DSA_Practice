# LeetCode 1878 - Get Biggest Three Rhombus Sums in a Grid

from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = set()

        for r in range(m):
            for c in range(n):
                # size 0 rhombus
                res.add(grid[r][c])

                k = 1
                while True:
                    if r-k < 0 or r+k >= m or c-k < 0 or c+k >= n:
                        break

                    s = 0

                    # top -> right
                    i, j = r-k, c
                    for t in range(k):
                        s += grid[i+t][j+t]

                    # right -> bottom
                    i, j = r, c+k
                    for t in range(k):
                        s += grid[i+t][j-t]

                    # bottom -> left
                    i, j = r+k, c
                    for t in range(k):
                        s += grid[i-t][j-t]

                    # left -> top
                    i, j = r, c-k
                    for t in range(k):
                        s += grid[i-t][j+t]

                    res.add(s)
                    k += 1

        return sorted(res, reverse=True)[:3]
