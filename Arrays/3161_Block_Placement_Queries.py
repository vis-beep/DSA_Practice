from bisect import bisect_left, bisect_right
from sortedcontainers import SortedList

class FenwickMax:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & -idx

    def query(self, idx):
        idx += 1
        res = 0
        while idx > 0:
            res = max(res, self.bit[idx])
            idx -= idx & -idx
        return res


class Solution:
    def getResults(self, queries):
        mx = 0
        obstacles = set()

        for q in queries:
            mx = max(mx, q[1])
            if q[0] == 1:
                obstacles.add(q[1])

        LIMIT = mx + 1

        sl = SortedList([0, LIMIT])
        for x in obstacles:
            sl.add(x)

        bit = FenwickMax(LIMIT + 2)

        for i in range(1, len(sl)):
            bit.update(sl[i], sl[i] - sl[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                x, sz = q[1], q[2]

                idx = sl.bisect_right(x) - 1
                p = sl[idx]

                best = max(bit.query(p), x - p)
                ans.append(best >= sz)

            else:
                x = q[1]

                idx = sl.bisect_left(x)

                prev_obs = sl[idx - 1]
                next_obs = sl[idx + 1]

                bit.update(next_obs, next_obs - prev_obs)

                sl.remove(x)

        return ans[::-1]
