package leetcode;

import java.util.Arrays;
import org.junit.Test;

import static junit.framework.TestCase.assertTrue;

public class L0001TwoSumTest {

  final L0001TwoSum solution = new L0001TwoSum();

  @Test
  public void test() {
    assertTrue(Arrays.equals(new int[] {0, 2}, solution.twoSum(new int[] {1, 2, 3}, 4)));
  }

}