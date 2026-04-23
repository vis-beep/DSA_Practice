import java.util.*;

class Solution {
    public long[] distance(int[] nums) {
        int n = nums.length;
        long[] ans = new long[n];
        
        // Store indices for each value
        Map<Integer, List<Integer>> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            map.computeIfAbsent(nums[i], k -> new ArrayList<>()).add(i);
        }
        
        // Process each group of same values
        for (List<Integer> list : map.values()) {
            int size = list.size();
            
            // Prefix sum of indices
            long[] prefix = new long[size];
            prefix[0] = list.get(0);
            
            for (int i = 1; i < size; i++) {
                prefix[i] = prefix[i - 1] + list.get(i);
            }
            
            for (int i = 0; i < size; i++) {
                long leftSum = 0, rightSum = 0;
                int idx = list.get(i);
                
                // Left side contribution
                if (i > 0) {
                    leftSum = (long) i * idx - prefix[i - 1];
                }
                
                // Right side contribution
                if (i < size - 1) {
                    rightSum = (prefix[size - 1] - prefix[i]) - (long) (size - i - 1) * idx;
                }
                
                ans[idx] = leftSum + rightSum;
            }
        }
        
        return ans;
    }
}
