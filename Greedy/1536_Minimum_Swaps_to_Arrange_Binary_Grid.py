"""
Problem: Minimum Swaps to Arrange a Binary Grid
Category: Greedy
Time Complexity: O(n^2)
"""

class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Count trailing zeros
        trailing = []
        for row in grid:
            count = 0
            for j in range(n - 1, -1, -1):
                if row[j] == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Greedy placement
        for i in range(n):
            required = n - i - 1
            j = i
            
            while j < n and trailing[j] < required:
                j += 1
            
            if j == n:
                return -1
            
            while j > i:
                trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps
