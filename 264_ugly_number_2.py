# Use a heap.
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        import heapq
        nums = [(2, 2), (3, 3), (5, 5)]
        i = 1
        while i < n:
            num, last_multiplier = heapq.heappop(nums)
            if last_multiplier == 2:
                heapq.heappush(nums, (num*2, 2))
                heapq.heappush(nums, (num*3, 3))
                heapq.heappush(nums, (num*5, 5))
            elif last_multiplier == 3:
                heapq.heappush(nums, (num*3, 3))
                heapq.heappush(nums, (num*5, 5))
            else:
                heapq.heappush(nums, (num*5, 5))
            i += 1
        return num

