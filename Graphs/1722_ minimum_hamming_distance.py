from collections import defaultdict, Counter

class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        
        # Step 1: Union-Find
        parent = list(range(len(source)))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                parent[py] = px
        
        # Build components
        for a, b in allowedSwaps:
            union(a, b)
        
        # Step 2: Group indices
        groups = defaultdict(list)
        for i in range(len(source)):
            groups[find(i)].append(i)
        
        # Step 3: Calculate answer
        ans = 0
        
        for indices in groups.values():
            freq = Counter()
            
            for i in indices:
                freq[source[i]] += 1
            
            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    ans += 1
        
        return ans
