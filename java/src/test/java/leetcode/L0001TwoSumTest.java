package leetcode;

import java.util.Arrays;
import org.junit.Test;

import static junit.framework.TestCase.assertTrue;

public class L0001TwoSumTest {

  final L0001TwoSum solution = new L0001TwoSum();

  @Test
  public void test() {
    assertTrue(Arrays.equals(new int[] {0, 1}, solution.twoSum(new int[] {2, 7, 11, 15}, 9)));
  }

}