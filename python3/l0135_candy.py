from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [0] * len(ratings)
        candies[0] = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
            else:
                candies[i] = 1
        
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i+1] + 1, candies[i])
                
        return sum(candies)