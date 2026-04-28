Given a 2D integer grid and an integer x, the task is to make all grid elements equal by either adding or subtracting x in one operation.

### 💡 Approach:

* Flatten the 2D grid into a 1D list
* Check if all elements have the same remainder when divided by x
  → If not, return `-1` since it's impossible
* Sort the list and choose the median as the target value
  → Median gives minimum total operations
* Count operations using:

operations += abs(num - median) // x

### ✅ Time Complexity:

* Sorting: **O(n log n)**
* Traversal: **O(n)**

Overall: **O(n log n)**

### 🐍 Python Code:

```python
class Solution:
    def minOperations(self, grid, x):
        nums = []

        for row in grid:
            for val in row:
                nums.append(val)

        rem = nums[0] % x
        for num in nums:
            if num % x != rem:
                return -1

        nums.sort()
        median = nums[len(nums) // 2]

        operations = 0
        for num in nums:
            operations += abs(num - median) // x

        return operations
```

#Python #LeetCode #DSA #Algorithms #CodingInterview #ProblemSolving #Programming #SoftwareEngineering
