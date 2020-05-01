class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    def numWays(self, n, k):
        # write your code her
        if n == 1:
            return k
        same = k  # previous 2 has same color
        diff = k * (k - 1)  # previous 2 has diff color
        for i in range(3, n+1):
            # If same, can only paint k-1 next round, all will have diff color.
            # If diff, can paint k next round, of which 1/k have same color.
            new_same = diff
            new_diff = same * (k - 1) + diff * (k - 1)
            same = new_same
            diff = new_diff
        return same + diff
