class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_product = 1

        while temp > 0:
            digit = temp % 10

            digit_sum += digit
            digit_product *= digit

            temp //= 10

        divisor = digit_sum + digit_product

        return n % divisor == 0
