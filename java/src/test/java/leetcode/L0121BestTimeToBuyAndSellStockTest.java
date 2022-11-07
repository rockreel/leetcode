package leetcode;

import org.junit.Test;

import static org.junit.Assert.*;

public class L0121BestTimeToBuyAndSellStockTest {

    L0121BestTimeToBuyAndSellStock solution = new L0121BestTimeToBuyAndSellStock();

    @Test
    public void test() {
        assertEquals(
                5,
                solution.maxProfit(new int[] { 7, 1, 5, 3, 6, 4 }));

        assertEquals(
                0,
                solution.maxProfit(new int[] { 7, 6, 4, 3, 1 }));

    }

}
