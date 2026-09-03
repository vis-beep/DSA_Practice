class Solution:

    def uniformArray(self, nums1: list[int]) -> bool:
        min_val = min(nums1)

        # If the smallest element is odd, we can always make all elements odd.
        if min_val % 2 != 0:
            return True

        # If the smallest element is even, all other elements MUST also be even.
        # If any element is odd, it's impossible to make it even.
        return all(x % 2 == 0 for x in nums1)
