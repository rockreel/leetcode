package leetcode;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class L0053MaximumSubarrayTest {

    L0053MaximumSubarray solution = new L0053MaximumSubarray();

    @Test
    public void test() {
        assertEquals(
                6,
                solution.maxSubArray(new int[] { -2, 1, -3, 4, -1, 2, 1, -5, 4 }));
        assertEquals(
                1,
                solution.maxSubArray(new int[] { 1 }));
        assertEquals(
                23,
                solution.maxSubArray(new int[] { 5, 4, -1, 7, 8 }));
    }

}
