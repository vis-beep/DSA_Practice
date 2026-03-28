class Solution:
    def findTheString(self, lcp):
        n = len(lcp)
        
        # Step 1: DSU (Union-Find)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Union indices where lcp > 0
        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)
        
        # Step 2: Assign characters (lexicographically smallest)
        group_char = {}
        res = [''] * n
        current_char = 'a'
        
        for i in range(n):
            root = find(i)
            if root not in group_char:
                if current_char > 'z':
                    return ""
                group_char[root] = current_char
                current_char = chr(ord(current_char) + 1)
            res[i] = group_char[root]
        
        word = ''.join(res)
        
        # Step 3: Validate LCP matrix
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = 0
        
        # Check validity
        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""
        
        return word
