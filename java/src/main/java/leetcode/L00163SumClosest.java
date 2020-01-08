package leetcode;

import java.util.Arrays;

public class L00163SumClosest {

  public int threeSumClosest(int[] nums, int target) {
    Arrays.sort(nums);
    int minDiff = Integer.MAX_VALUE;
    int closestTarget = Integer.MAX_VALUE;
    for (int i = 0; i < nums.length - 2; i++) {
      int twoTarget = twoSumClosest(nums, i+1, nums.length-1, target-nums[i]);
      int threeTarget = nums[i] + twoTarget;
      if (Math.abs(target - threeTarget) < minDiff) {
        minDiff = Math.abs(target - threeTarget);
        closestTarget = threeTarget;
      }
    }
    return closestTarget;
  }

  public int twoSumClosest(int[] nums, int start, int end, int target) {
    int i = start, j = end;
    int minDiff = Integer.MAX_VALUE;
    int closestTarget = Integer.MAX_VALUE;
    while (i < j) {
      if (Math.abs(target - (nums[i] + nums[j])) < minDiff) {
        minDiff = Math.abs(target - (nums[i] + nums[j]));
        closestTarget = nums[i] + nums[j];
      }
      if (nums[i] + nums[j] > target) {
        j--;
      } else if (nums[i] + nums[j] < target) {
        i++;
      } else {
        return target;
      }
    }
    return closestTarget;
  }

}
