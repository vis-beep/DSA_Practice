class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')
        
        for i in range(n):
            if words[i] == target:
                right = (i - startIndex + n) % n
                left = (startIndex - i + n) % n
                ans = min(ans, right, left)
        
        return ans if ans != float('inf') else -1
