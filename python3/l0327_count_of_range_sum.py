import bisect

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:

        range_sum = [0]
        sum_ = 0
        num = 0
        for i, n in enumerate(nums):
            sum_ += n
            lower_bound = bisect.bisect_left(range_sum, sum_ - upper)
            upper_bound = bisect.bisect_right(range_sum, sum_ - lower)
            num += upper_bound - lower_bound
            bisect.insort_left(range_sum, sum_)
        return num

