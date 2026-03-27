class Solution:
    def areSimilar(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        
        # Reduce shifts using modulo
        k = k % n
        
        for i in range(m):
            for j in range(n):
                
                if i % 2 == 0:
                    # Even row → left cyclic shift
                    new_j = (j + k) % n
                else:
                    # Odd row → right cyclic shift
                    new_j = (j - k) % n
                
                if mat[i][j] != mat[i][new_j]:
                    return False
        
        return True
