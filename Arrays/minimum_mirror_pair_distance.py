from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        """
        Finds the minimum distance between indices (i, j)
        such that reverse(nums[i]) == nums[j].

        Approach:
        - Use a hashmap to store reversed values as keys
        - For each number, check if it exists in the map
        - If yes, compute distance and update minimum
        - Store reversed number for future matches

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        reverse_map = {}  # stores {value_to_match: index}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            # Check if current number matches any previously stored reverse
            if num in reverse_map:
                min_dist = min(min_dist, i - reverse_map[num])

            # Store the reversed value for future matches
            reversed_num = int(str(num)[::-1])
            reverse_map[reversed_num] = i

        return min_dist if min_dist != float('inf') else -1


# Optional: quick test
if __name__ == "__main__":
    sol = Solution()
    print(sol.minMirrorPairDistance([12, 21, 45, 33, 54]))  # Output: 1
    print(sol.minMirrorPairDistance([120, 21]))             # Output: 1
    print(sol.minMirrorPairDistance([21, 120]))             # Output: -1
