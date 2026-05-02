"""
LeetCode 788 - Rotated Digits

Problem:
An integer is good if after rotating each digit individually by 180 degrees,
we get a valid number that is different from the original.

Valid rotations:
0->0, 1->1, 8->8
2<->5, 6<->9

Approach:
- Iterate from 1 to n
- Check if each number:
  1. Contains only valid digits
  2. Contains at least one digit that changes (2,5,6,9)
- Count such numbers

Time Complexity: O(n * d)
Space Complexity: O(1)
"""

class Solution:
    def rotatedDigits(self, n: int) -> int:
        valid = {'0', '1', '2', '5', '6', '8', '9'}
        change = {'2', '5', '6', '9'}
        
        count = 0
        
        for num in range(1, n + 1):
            s = str(num)
            is_valid = True
            is_changed = False
            
            for ch in s:
                if ch not in valid:
                    is_valid = False
                    break
                if ch in change:
                    is_changed = True
            
            if is_valid and is_changed:
                count += 1
        
        return count


# Example usage
if __name__ == "__main__":
    n = 10
    print(Solution().rotatedDigits(n))  # Output: 4
