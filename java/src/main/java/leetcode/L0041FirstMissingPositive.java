package leetcode;

import java.lang.Math;

public class L0041FirstMissingPositive {

    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        
        // Mark every number not in range [1, n] with a number (n+1) 
        // that is not going to be the first missing number.
        for (int i = 0; i < n; i++) {
            if (nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;
            }
        }
        
        // For each number, mark the index of that number corresponds to
        // negative.
        for (int i = 0; i < n; i++) {
            int num = Math.abs(nums[i]);
            if (num > n) {
                continue;
            }
            if (nums[num-1] > 0) {
                nums[num-1] = -nums[num-1];
            }
        }
        
        // Find the first non-negative number that is the result.
        for (int i = 0; i < n; i++) {
            if (nums[i] > 0) {
                return i + 1;
            }
        }
        return n + 1;
    }
    
}
