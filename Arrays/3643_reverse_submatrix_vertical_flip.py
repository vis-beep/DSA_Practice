"""
Problem: Reverse (Flip) a k x k Submatrix Vertically

Given an m x n matrix, and integers x, y, k:
- (x, y) represents the top-left corner of a k x k submatrix
- Flip the submatrix vertically (reverse row order)

Approach:
- Swap rows within the submatrix:
    First row ↔ Last row
    Second row ↔ Second last row, etc.

Time Complexity: O(k^2)
Space Complexity: O(1)
"""


class Solution:
    def reverseSubmatrix(self, grid, x, y, k):
        """
        Reverses a k x k submatrix vertically in-place.

        :param grid: List[List[int]] - Input matrix
        :param x: int - Starting row index
        :param y: int - Starting column index
        :param k: int - Size of square submatrix
        :return: List[List[int]] - Updated matrix
        """

        for i in range(k // 2):
            top_row = x + i
            bottom_row = x + k - 1 - i

            for j in range(k):
                col = y + j
                grid[top_row][col], grid[bottom_row][col] = (
                    grid[bottom_row][col],
                    grid[top_row][col],
                )

        return grid


# Optional: Local testing
if __name__ == "__main__":
    grid = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    x, y, k = 1, 0, 3

    sol = Solution()
    result = sol.reverseSubmatrix(grid, x, y, k)

    for row in result:
        print(row)
