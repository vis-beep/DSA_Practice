class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])

        found = False
        for idx, _ in restrictions:
            if idx == n:
                found = True
                break

        if not found:
            restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # Left -> Right
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] + dist
            )

        # Right -> Left
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] + dist
            )

        ans = 0

        for i in range(1, m):
            x1, h1 = restrictions[i - 1]
            x2, h2 = restrictions[i]

            dist = x2 - x1

            peak = (h1 + h2 + dist) // 2
            ans = max(ans, peak)

        return ans
