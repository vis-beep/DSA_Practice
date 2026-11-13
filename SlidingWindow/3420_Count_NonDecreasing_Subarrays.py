
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        dq = deque()
        n = len(nums)

        right = n - 1
        cost = 0
        ans = 0

        for left in range(n - 1, -1, -1):
            x = nums[left]
            count = 0

            while dq and dq[0][0] <= x:
                val, cnt = dq.popleft()
                cost += (x - val) * cnt
                count += cnt

            if count:
                dq.appendleft((x, count))

            while cost > k:
                val, cnt = dq[-1]
                cost -= val - nums[right]

                cnt -= 1
                right -= 1

                if cnt == 0:
                    dq.pop()
                else:
                    dq[-1] = (val, cnt)

            ans += right - left + 1

            dq.appendleft((x, 1))

        return ans
