# Use an array.
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1]
        i2, i3, i5 = 0, 0, 0
        while len(nums) < n:
            m2 = nums[i2] * 2
            m3 = nums[i3] * 3
            m5 = nums[i5] * 5
            m = min(m2, m3, m5)
            nums.append(m)
            if m == m2:
                i2 += 1
            if m == m3:
                i3 += 1
            if m == m5:
                i5 += 1
        return nums[-1]

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

