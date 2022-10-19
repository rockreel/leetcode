package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0210CouseSchedule2Test {

    L0210CouseSchedule2 solution = new L0210CouseSchedule2();

    @Test
    public void test() {
        assertArrayEquals(
                new int[] { 0, 1 },
                solution.findOrder(2, new int[][] { { 1, 0 } }));

        assertArrayEquals(
                new int[] { 0, 1, 2, 3 },
                solution.findOrder(4, new int[][] { { 1, 0 }, { 2, 0 }, { 3, 1 }, { 3, 2 } }));

        assertArrayEquals(
                new int[] { 0 },
                solution.findOrder(1, new int[][] {}));
    }

}
