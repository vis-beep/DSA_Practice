class Solution:
    def validSequence(self, word1: str, word2: str):
        n = len(word1)
        m = len(word2)

        # last[j] = position of the last selected character
        # when matching word2[j:] from right to left.
        last = [-1] * m

        i = n - 1
        j = m - 1

        while i >= 0 and j >= 0:
            if word1[i] == word2[j]:
                last[j] = i
                j -= 1
            i -= 1

        ans = []
        j = 0
        can_change = True

        for i in range(n):
            if j == m:
                break

            # Normal matching
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed character change
            elif can_change and (
                j == m - 1 or i < last[j + 1]
            ):
                ans.append(i)
                j += 1
                can_change = False

        return ans if j == m else []
