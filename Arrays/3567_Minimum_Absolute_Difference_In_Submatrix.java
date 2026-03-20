/**
 * Problem: Minimum Absolute Difference in k x k Submatrix
 * 
 * Approach:
 * 1. Iterate over all possible k x k submatrices
 * 2. Collect elements into a list
 * 3. Sort the list
 * 4. Compute minimum absolute difference between distinct adjacent elements
 * 
 * Time Complexity: O((m-k+1)*(n-k+1) * k^2 log(k^2))
 * Space Complexity: O(k^2)
 */

import java.util.*;

public class MinAbsDiffSubmatrix {

    public int[][] minAbsDiff(int[][] grid, int k) {
        int m = grid.length, n = grid[0].length;
        int[][] ans = new int[m - k + 1][n - k + 1];

        for (int i = 0; i <= m - k; i++) {
            for (int j = 0; j <= n - k; j++) {

                List<Integer> list = new ArrayList<>();

                // Collect elements of submatrix
                for (int x = i; x < i + k; x++) {
                    for (int y = j; y < j + k; y++) {
                        list.add(grid[x][y]);
                    }
                }

                // Sort elements
                Collections.sort(list);

                int minDiff = Integer.MAX_VALUE;
                boolean found = false;

                // Find minimum difference between distinct elements
                for (int t = 1; t < list.size(); t++) {
                    if (list.get(t).equals(list.get(t - 1))) continue;

                    minDiff = Math.min(minDiff, list.get(t) - list.get(t - 1));
                    found = true;
                }

                // If all elements are same
                ans[i][j] = found ? minDiff : 0;
            }
        }

        return ans;
    }
}
