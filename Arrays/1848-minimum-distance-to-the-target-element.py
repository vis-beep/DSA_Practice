class Solution:
    def getMinDistance(self, nums, target, start):
        """
        Finds the minimum absolute distance between start index
        and any index i such that nums[i] == target.

        :param nums: List[int]
        :param target: int
        :param start: int
        :return: int
        """
        min_dist = float('inf')

        for i in range(len(nums)):
            if nums[i] == target:
                min_dist = min(min_dist, abs(i - start))

        return min_dist


# Example usage
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    target = 5
    start = 3

    sol = Solution()
    print(sol.getMinDistance(nums, target, start))  # Output: 1
