class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        min_sum = [0] * len(triangle)
            
        for i, row in enumerate(triangle):
            for j, n in enumerate(row):
                min_sum_j = min_sum[j]
                if j == 0:
                    min_sum[j] = n + min_sum_j
                elif j == i:
                    min_sum[j] = n + min_sum_j_1
                else:
                    min_sum[j] = n + min(min_sum_j_1, min_sum_j)
                min_sum_j_1 = min_sum_j
                    
        return min(min_sum)

