package leetcode;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class L0039CombinationSum {
    private List<List<Integer>> combination(int[] candidates, int target, int start) {
        if (target == 0) {
            return Arrays.asList(new ArrayList<Integer>());
        }
        List<List<Integer>> result = new ArrayList<>();
        for (int i = start; i < candidates.length; i++) {
            int candidate = candidates[i];
            if (candidate > target) {
                continue;
            }
            for (List<Integer> r : combination(candidates, target-candidate, i)) {
                List<Integer> comb = new ArrayList<Integer>();
                comb.add(candidate);
                comb.addAll(r);
                result.add(comb);
            }
        }
        return result;
    }
  
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        return combination(candidates, target, 0);  
    }
}
