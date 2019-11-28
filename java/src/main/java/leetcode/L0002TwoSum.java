package leetcode;

import java.util.HashMap;
import java.util.Map;

class L0002TwoSum {

    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(nums[i])) {
                return new int[] { map.get(nums[i]), i };
            } else {
                map.put(target - nums[i], i);
            }
        }
        throw new RuntimeException("Can not find two numbers for the target.");
    }

}
