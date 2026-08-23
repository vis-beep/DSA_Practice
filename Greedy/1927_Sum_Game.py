class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        diff = left_sum - right_sum

        # Odd number of '?' -> Alice wins
        if (left_q + right_q) % 2 == 1:
            return True

        # Check whether Bob can force equal sums
        return diff != 9 * (right_q - left_q) // 2
