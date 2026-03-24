class Solution:
    def constructProductMatrix(self, grid):
        MOD = 12345
        n, m = len(grid), len(grid[0])
        
        # Flatten grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = len(arr)
        
        # Prefix product
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i - 1] * arr[i - 1]) % MOD
        
        # Suffix product
        suffix = [1] * size
        for i in range(size - 2, -1, -1):
            suffix[i] = (suffix[i + 1] * arr[i + 1]) % MOD
        
        # Compute result
        result = [0] * size
        for i in range(size):
            result[i] = (prefix[i] * suffix[i]) % MOD
        
        # Convert back to 2D
        res = []
        idx = 0
        for i in range(n):
            row = []
            for j in range(m):
                row.append(result[idx])
                idx += 1
            res.append(row)
        
        return res
