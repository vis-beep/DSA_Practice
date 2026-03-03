LC-1545
- Applied recursive divide and conquer approach
- Used mirror index symmetry observation
- Time Complexity: O(n)
- Space Complexity: O(n)
class Solution:
    def findKthBit(self, n, k):
        if n == 1:
            return "0"
        
        mid = 2 ** (n - 1)
        
        if k == mid:
            return "1"
        
        if k < mid:
            return self.findKthBit(n - 1, k)
        
        mirrored = 2 ** n - k
        bit = self.findKthBit(n - 1, mirrored)
        
        return "1" if bit == "0" else "0"


# 🔽 For Local Testing (GitHub / VS Code)
if __name__ == "__main__":
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    
    solution = Solution()
    result = solution.findKthBit(n, k)
    
    print("Kth Bit:", result)
