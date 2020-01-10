class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # Minimum candies to satisfy each one's left neighbor.
        candies_left = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies_left[i] = candies_left[i-1] + 1
        # Minimum candies to satisfy each one's right neighbor.
        candies_right = [1] * len(ratings)
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies_right[i] = candies_right[i+1] + 1

        return sum([max(l, r) for l, r in zip(candies_left, candies_right)])

