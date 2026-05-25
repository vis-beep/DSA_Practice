from collections import deque

class Solution:
    def canReach(self, s, minJump, maxJump):
        n = len(s)
        queue = deque([0])
        farthest = 0

        while queue:
            i = queue.popleft()

            start = max(i + minJump, farthest + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):
                if s[j] == '0':
                    if j == n - 1:
                        return True
                    queue.append(j)

            farthest = end

        return n == 1
