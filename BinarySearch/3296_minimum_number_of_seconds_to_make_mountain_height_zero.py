import math

class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        
        def canFinish(T):
            total = 0
            
            for t in workerTimes:
                val = 1 + (8 * T) // t
                x = int((-1 + math.sqrt(val)) // 2)
                total += x
                
                if total >= mountainHeight:
                    return True
            
            return False

        left = 0
        right = min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = right

        while left <= right:
            mid = (left + right) // 2

            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans
