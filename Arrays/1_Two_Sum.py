"""
Problem: 1. Two Sum
Link: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Category: Arrays / Hashing

Approach:
We use a hashmap (dictionary) to store previously seen numbers and their indices.

For each element:
    - Calculate difference = target - current_number
    - If difference exists in hashmap → return indices
    - Otherwise store current number with index

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in hashmap:
                return [hashmap[diff], i]

            hashmap[num] = i
