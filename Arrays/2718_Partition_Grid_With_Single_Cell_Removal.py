Readme 

    ## Grid Partition with Single Cell Removal

This problem checks whether a grid can be split into two parts (horizontal or vertical cut) such that:

- Both parts have equal sum OR
- Equal sum can be achieved by removing at most one cell
- The remaining section must stay connected

### Approach
- Prefix sum for fast partition sum calculation
- Hash maps + binary search to efficiently check value existence
- Special handling for 1D edge cases (single row/column)

### Complexity
- Time: O(m*n + (m+n) log n)
- Space: O(m*n)


CODE:

from collections import defaultdict
import bisect

class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = sum(grid[i][j] for i in range(m) for j in range(n))

        # ── Horizontal cuts ────────────────────────────────────────────────
        val_rows = defaultdict(list)
        for i in range(m):
            for v in set(grid[i]):
                val_rows[v].append(i)

        def in_top(val, max_row):
            rows = val_rows.get(val, [])
            return bisect.bisect_right(rows, max_row) > 0

        def in_bottom(val, min_row):
            rows = val_rows.get(val, [])
            return bisect.bisect_left(rows, min_row) < len(rows)

        row_prefix = [0] * (m + 1)
        for i in range(m):
            row_prefix[i + 1] = row_prefix[i] + sum(grid[i])

        for i in range(m - 1):
            top = row_prefix[i + 1]
            bottom = total - top

            if top == bottom:
                return True

            diff = abs(top - bottom)
            top_rows = i + 1
            bottom_rows = m - i - 1

            if top > bottom:
                if top_rows >= 2 and n >= 2:
                    if in_top(diff, i):
                        return True
                elif top_rows == 1 and n >= 2:
                    if grid[0][0] == diff or grid[0][n - 1] == diff:
                        return True
                elif n == 1 and top_rows >= 2:
                    if grid[0][0] == diff or grid[i][0] == diff:
                        return True
            else:
                if bottom_rows >= 2 and n >= 2:
                    if in_bottom(diff, i + 1):
                        return True
                elif bottom_rows == 1 and n >= 2:
                    if grid[m - 1][0] == diff or grid[m - 1][n - 1] == diff:
                        return True
                elif n == 1 and bottom_rows >= 2:
                    if grid[i + 1][0] == diff or grid[m - 1][0] == diff:
                        return True

        # ── Vertical cuts ─────────────────────────────────────────────────
        val_cols = defaultdict(list)
        for j in range(n):
            for v in set(grid[i][j] for i in range(m)):
                val_cols[v].append(j)

        def in_left(val, max_col):
            cols = val_cols.get(val, [])
            return bisect.bisect_right(cols, max_col) > 0

        def in_right(val, min_col):
            cols = val_cols.get(val, [])
            return bisect.bisect_left(cols, min_col) < len(cols)

        col_prefix = [0] * (n + 1)
        for j in range(n):
            col_prefix[j + 1] = col_prefix[j] + sum(grid[i][j] for i in range(m))

        for j in range(n - 1):
            left = col_prefix[j + 1]
            right = total - left

            if left == right:
                return True

            diff = abs(left - right)
            left_cols = j + 1
            right_cols = n - j - 1

            if left > right:
                if m >= 2 and left_cols >= 2:
                    if in_left(diff, j):
                        return True
                elif m == 1 and left_cols >= 2:
                    if grid[0][0] == diff or grid[0][j] == diff:
                        return True
                elif left_cols == 1 and m >= 2:
                    if grid[0][0] == diff or grid[m - 1][0] == diff:
                        return True
            else:
                if m >= 2 and right_cols >= 2:
                    if in_right(diff, j + 1):
                        return True
                elif m == 1 and right_cols >= 2:
                    if grid[0][j + 1] == diff or grid[0][n - 1] == diff:
                        return True
                elif right_cols == 1 and m >= 2:
                    if grid[0][j + 1] == diff or grid[m - 1][j + 1] == diff:
                        return True

        return False
    
