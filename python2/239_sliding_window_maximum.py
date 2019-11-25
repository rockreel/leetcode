class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        queue = deque()
        maximums = []
        for i, n in enumerate(nums):
            while queue and nums[queue[-1]] < n:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                maximums.append(nums[queue[0]])
                if queue[0] <= i - k + 1:
                    queue.popleft()
        return maximums

