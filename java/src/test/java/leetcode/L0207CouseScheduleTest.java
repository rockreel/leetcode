package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0207CouseScheduleTest {

  L0207CouseSchedule solution = new L0207CouseSchedule();

  @Test
  public void test() {
    assertTrue(
        solution.canFinish(2, new int[][] {{1, 0}})
    );

    assertFalse(
        solution.canFinish(2, new int[][] {{1, 0}, {0, 1}})
    );

  }

}
