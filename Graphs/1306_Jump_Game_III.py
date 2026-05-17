class Solution:
    def canReach(self, arr, start):
        n = len(arr)
        visited = [False] * n

        def dfs(i):
            # Out of bounds or already visited
            if i < 0 or i >= n or visited[i]:
                return False

            # Reached index with value 0
            if arr[i] == 0:
                return True

            visited[i] = True

            # Explore forward and backward jumps
            return dfs(i + arr[i]) or dfs(i - arr[i])

        return dfs(start)


# Example Usage
arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

obj = Solution()
print(obj.canReach(arr, start))
