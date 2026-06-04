class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def waviness(num: int) -> int:
            digits = str(num)
            n = len(digits)

            if n < 3:
                return 0

            count = 0

            for i in range(1, n - 1):
                left = int(digits[i - 1])
                curr = int(digits[i])
                right = int(digits[i + 1])

                if (curr > left and curr > right) or \
                   (curr < left and curr < right):
                    count += 1

            return count

        return sum(waviness(num) for num in range(num1, num2 + 1))
