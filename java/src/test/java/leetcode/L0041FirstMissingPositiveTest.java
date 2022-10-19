package leetcode;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class L0041FirstMissingPositiveTest {

  L0041FirstMissingPositive solution = new L0041FirstMissingPositive();

  @Test
  public void test() {
    assertEquals(
      3,
      solution.firstMissingPositive(new int[]{1, 2, 0})
    );
    assertEquals(
      2,
      solution.firstMissingPositive(new int[]{3, 4, -1, 1})
    );
    assertEquals(
      1,
      solution.firstMissingPositive(new int[]{7, 8, 9, 11, 12})
    );
  }

}
