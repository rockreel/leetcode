package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class L00153Sum {

  public List<List<Integer>> threeSum(int[] nums) {
    Arrays.sort(nums);
    List<List<Integer>> result = new ArrayList();
    int i = 0;
    while (i + 1 < nums.length) {
      findResult(-nums[i], nums, i + 1, result);
      while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
        i++;
      }
      i++;
    }
    return result;
  }

  private void findResult(int target, int[] nums, int startIdx, List<List<Integer>> result) {
    int i = startIdx, j = nums.length - 1;
    while (i < j) {
      if (nums[i] + nums[j] > target) {
        j--;
      } else if (nums[i] + nums[j] < target) {
        i++;
      } else {
        result.add(Arrays.asList(-target, nums[i], nums[j]));
        while (nums[j - 1] == nums[j] && j - 1 > 0) {
          j--;
        }
        while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
          i++;
        }
        i++;
        j--;
      }
    }
  }

}

