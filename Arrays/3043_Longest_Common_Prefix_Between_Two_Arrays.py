class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()

        # Store all prefixes from arr1
        for num in arr1:
            num = str(num)

            for i in range(1, len(num) + 1):
                prefixes.add(num[:i])

        longest = 0

        # Find longest common prefix using arr2
        for num in arr2:
            num = str(num)

            for i in range(1, len(num) + 1):
                if num[:i] in prefixes:
                    longest = max(longest, i)

        return longest
