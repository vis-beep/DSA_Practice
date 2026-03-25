class Solution:
    def canPartitionGrid(self, grid):
        """
        Determines if a single horizontal or vertical cut can divide the grid
        into two non-empty parts with equal sums.

        :param grid: List[List[int]]
        :return: bool
        """
        m, n = len(grid), len(grid[0])

        # Compute total sum of grid
        total_sum = sum(sum(row) for row in grid)

        # If total sum is odd, equal partition is impossible
        if total_sum % 2 != 0:
            return False

        # -------- Horizontal Cut Check --------
        prefix_sum = 0
        for i in range(m - 1):  # ensure bottom part is non-empty
            prefix_sum += sum(grid[i])
            if prefix_sum == total_sum - prefix_sum:
                return True

        # -------- Vertical Cut Check --------
        col_sums = [0] * n
        for j in range(n):
            for i in range(m):
                col_sums[j] += grid[i][j]

        prefix_sum = 0
        for j in range(n - 1):  # ensure right part is non-empty
            prefix_sum += col_sums[j]
            if prefix_sum == total_sum - prefix_sum:
                return True

        return False
