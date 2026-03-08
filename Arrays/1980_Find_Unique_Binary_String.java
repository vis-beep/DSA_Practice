/**
 * Problem: Find Unique Binary String
 *
 * Given an array of n unique binary strings of length n,
 * return a binary string of length n that does not appear in nums.
 *
 * Approach:
 * We use Cantor's Diagonalization method.
 * For each index i, flip the i-th character of nums[i].
 * This guarantees the generated string differs from every string
 * in the array at least at one position.
 *
 * Time Complexity: O(n)
 * Space Complexity: O(n)
 */

class Solution {

    public String findDifferentBinaryString(String[] nums) {

        int n = nums.length;
        StringBuilder result = new StringBuilder();

        for (int i = 0; i < n; i++) {

            // Flip the diagonal character
            if (nums[i].charAt(i) == '0') {
                result.append('1');
            } else {
                result.append('0');
            }
        }

        return result.toString();
    }
}
