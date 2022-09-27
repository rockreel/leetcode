package leetcode;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class L00163SumClosestTest {

  L00163SumClosest solution = new L00163SumClosest();

  @Test
  public void test() {
    assertEquals(
        2,
        solution.threeSumClosest(new int[] {-1, 2, 1, -4}, 1)
    );

    assertEquals(
        2,
        solution.threeSumClosest(new int[] {1, 1, 1, 0}, -100)
    );

  }

}
