class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        seenA = set()
        seenB = set()
        result = []

        for i in range(n):
            seenA.add(A[i])
            seenB.add(B[i])

            result.append(len(seenA & seenB))

        return result


# Example Usage
A = [1, 3, 2, 4]
B = [3, 1, 2, 4]

sol = Solution()
print(sol.findThePrefixCommonArray(A, B))
