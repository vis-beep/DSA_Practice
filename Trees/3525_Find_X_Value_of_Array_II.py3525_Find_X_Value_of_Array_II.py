class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Each node:
        # [product of segment % k, count of prefix products]
        #
        # cnt[r] = number of non-empty prefixes
        # whose product % k == r

        def merge(A, B):
            prodA = A[0]
            prodB = B[0]

            cnt = [0] * k

            # Prefixes completely inside A
            for r in range(k):
                cnt[r] += A[1][r]

            # Prefixes = whole A + prefix of B
            for r in range(k):
                nr = (prodA * r) % k
                cnt[nr] += B[1][r]

            prod = (prodA * prodB) % k

            return [prod, cnt]

        # Identity node for an empty segment
        identity = [1 % k, [0] * k]

        # Segment tree
        size = 1
        while size < n:
            size *= 2

        tree = [identity[:] for _ in range(2 * size)]

        # Build leaves
        for i in range(n):
            v = nums[i] % k

            cnt = [0] * k
            cnt[v] = 1

            tree[size + i] = [v, cnt]

        # Build tree
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, value):
            idx = size + pos
            v = value % k

            cnt = [0] * k
            cnt[v] = 1

            tree[idx] = [v, cnt]

            idx //= 2

            while idx:
                tree[idx] = merge(tree[2 * idx], tree[2 * idx + 1])
                idx //= 2

        def query(left, right):
            """
            Query inclusive range [left, right].
            """
            left += size
            right += size + 1

            left_result = identity
            right_result = identity

            while left < right:

                if left & 1:
                    left_result = merge(left_result, tree[left])
                    left += 1

                if right & 1:
                    right -= 1
                    right_result = merge(tree[right], right_result)

                left //= 2
                right //= 2

            return merge(left_result, right_result)

        result = []

        for index, value, start, x in queries:

            # Persistent update
            update(index, value)

            # Prefix-product distribution of nums[start...n-1]
            node = query(start, n - 1)

            result.append(node[1][x])

        return result
