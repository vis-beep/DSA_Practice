from collections import deque, defaultdict
from math import isqrt
from typing import List

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0

        MAXV = max(nums)

        # Sieve for prime checking
        is_prime = [True] * (MAXV + 1)
        if MAXV >= 0:
            is_prime[0] = False
        if MAXV >= 1:
            is_prime[1] = False

        for i in range(2, isqrt(MAXV) + 1):
            if is_prime[i]:
                for j in range(i * i, MAXV + 1, i):
                    is_prime[j] = False

        # Map: divisor -> indices having nums[idx] divisible by divisor
        divisible_indices = defaultdict(list)

        for idx, val in enumerate(nums):
            temp = val
            factors = set()

            d = 2
            while d * d <= temp:
                if temp % d == 0:
                    factors.add(d)
                    while temp % d == 0:
                        temp //= d
                d += 1

            if temp > 1:
                factors.add(temp)

            for f in factors:
                divisible_indices[f].append(idx)

        # BFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True

        used_prime = set()
        steps = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # Adjacent moves
                for ni in (i - 1, i + 1):
                    if 0 <= ni < n and not visited[ni]:
                        visited[ni] = True
                        q.append(ni)

                # Prime teleportation
                val = nums[i]

                if is_prime[val] and val not in used_prime:
                    for ni in divisible_indices[val]:
                        if not visited[ni]:
                            visited[ni] = True
                            q.append(ni)

                    used_prime.add(val)

            steps += 1

        return -1
