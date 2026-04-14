class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        memo = {}

        def dp(i, j):
            if i == n:
                return 0
            if j == m:
                return float('inf')

            if (i, j) in memo:
                return memo[(i, j)]

            # Option 1: skip factory
            res = dp(i, j + 1)

            # Option 2: assign robots
            pos, limit = factory[j]
            cost = 0

            for k in range(limit):
                if i + k >= n:
                    break
                cost += abs(robot[i + k] - pos)
                res = min(res, cost + dp(i + k + 1, j + 1))

            memo[(i, j)] = res
            return res

        return dp(0, 0)
