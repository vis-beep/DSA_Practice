# Jump Game IV

## Problem Statement
Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step you can jump from index `i` to:

- `i + 1` where `i + 1 < arr.length`
- `i - 1` where `i - 1 >= 0`
- `j` where `arr[i] == arr[j]` and `i != j`

Return the minimum number of steps to reach the last index of the array.

---

## Approach
We use **Breadth First Search (BFS)** because every jump represents one step.

### Key Idea
- Store all indices having the same value using a hashmap.
- From each index, explore:
  - Left index
  - Right index
  - Same value indices
- Use a visited array to avoid revisiting nodes.
- Clear processed lists to optimize performance.

---

## Time Complexity
- **O(n)**

## Space Complexity
- **O(n)**

---

## Python Solution

```python
from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        if n == 1:
            return 0

        mp = defaultdict(list)

        for i, val in enumerate(arr):
            mp[val].append(i)

        q = deque([0])
        visited = [False] * n
        visited[0] = True

        steps = 0

        while q:
            for _ in range(len(q)):
                idx = q.popleft()

                if idx == n - 1:
                    return steps

                next_indices = mp[arr[idx]] + [idx - 1, idx + 1]

                for ni in next_indices:
                    if 0 <= ni < n and not visited[ni]:
                        visited[ni] = True
                        q.append(ni)

                mp[arr[idx]].clear()

            steps += 1

        return -1
