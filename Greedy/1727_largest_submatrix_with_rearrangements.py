class Solution:
    def largestSubmatrix(self, matrix):
        m, n = len(matrix), len(matrix[0])
        height = [0] * n
        ans = 0

        for i in range(m):
            # build histogram heights
            for j in range(n):
                if matrix[i][j] == 1:
                    height[j] += 1
                else:
                    height[j] = 0

            # sort heights in descending order (simulate column rearrangement)
            sorted_heights = sorted(height, reverse=True)

            # compute max area
            for k in range(n):
                ans = max(ans, sorted_heights[k] * (k + 1))

        return ans
