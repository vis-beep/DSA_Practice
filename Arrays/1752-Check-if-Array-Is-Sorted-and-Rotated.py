# 1752. Check if Array Is Sorted and Rotated

## Problem
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

---

## Approach
An array is sorted and rotated if there is at most one position where the order decreases.

We count the number of times:

nums[i] > nums[(i + 1) % n]

If this count is greater than 1, the array cannot be sorted and rotated.

---

## Python Solution

```python
class Solution:
    def check(self, nums):
        count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        return count <= 1
