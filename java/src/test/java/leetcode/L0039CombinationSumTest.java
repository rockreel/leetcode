package leetcode;

import java.util.Arrays;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class L0039CombinationSumTest {

  L0039CombinationSum solution = new L0039CombinationSum();

  @Test
  public void test() {
    assertEquals(
      Arrays.asList(Arrays.asList(2, 2, 3), Arrays.asList(7)), 
      solution.combinationSum(new int[]{2, 3, 6, 7}, 7)
    );
  }

}
