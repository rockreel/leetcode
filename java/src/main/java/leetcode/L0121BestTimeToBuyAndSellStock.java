package leetcode;

public class L0121BestTimeToBuyAndSellStock {

    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int maxPriceOnRight = 0;
        int[] maxPricesOnRight = new int[prices.length];
        for (int i = prices.length - 1; i >= 0; i--) {
            maxPricesOnRight[i] = maxPriceOnRight;
            maxPriceOnRight = Math.max(prices[i], maxPriceOnRight);
            maxProfit = Math.max(maxPricesOnRight[i] - prices[i], maxProfit);
        }
        return maxProfit;
    }

}
