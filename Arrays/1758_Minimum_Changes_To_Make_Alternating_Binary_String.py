"""
LeetCode 1758
Minimum Changes To Make Alternating Binary String

Problem:
Given a binary string s, you can flip any character (0 -> 1 or 1 -> 0).
Return the minimum number of operations needed to make the string alternating.

Approach:
An alternating string can only be of two forms:
1. Starting with '0' -> 010101...
2. Starting with '1' -> 101010...

Count mismatches for both patterns and return the minimum.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minOperations(self, s: str) -> int:
        start_with_0 = 0
        start_with_1 = 0

        for i in range(len(s)):
            # pattern starting with 0 -> 0101...
            if s[i] != ('0' if i % 2 == 0 else '1'):
                start_with_0 += 1

            # pattern starting with 1 -> 1010...
            if s[i] != ('1' if i % 2 == 0 else '0'):
                start_with_1 += 1

        return min(start_with_0, start_with_1)
