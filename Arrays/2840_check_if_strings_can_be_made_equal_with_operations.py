"""
LeetCode 2840 - Check if Strings Can be Made Equal With Operations

Approach:
- We can only swap characters at indices where (j - i) is even.
- This means:
    * even indices can swap among themselves
    * odd indices can swap among themselves
- So we compare frequency of characters at:
    1. even indices
    2. odd indices
- If both match → return True

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution(object):
    def checkStrings(self, s1, s2):
        return (Counter(s1[::2]) == Counter(s2[::2]) and
                Counter(s1[1::2]) == Counter(s2[1::2]))
