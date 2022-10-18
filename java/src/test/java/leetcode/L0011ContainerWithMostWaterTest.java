package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0011ContainerWithMostWaterTest {

  L0011ContainerWithMostWater solution = new L0011ContainerWithMostWater();

  @Test
  public void test() {
    assertEquals(49, solution.maxArea(new int[] {1, 8, 6, 2, 5, 4, 8, 3, 7}));
  }

}
