class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller = sum(num < target for num in nums)
        count = nums.count(target)

        return list(range(smaller, smaller + count))
      
