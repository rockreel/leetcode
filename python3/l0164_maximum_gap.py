import math
from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        num_buckets = len(nums)
        upper_bound = max(nums) + 1
        lower_bound = min(nums)
        bucket_size = int(math.ceil(float(upper_bound-lower_bound)/float(num_buckets)))

        bucket_max = [None] * num_buckets
        bucket_min = [None] * num_buckets

        for n in nums:
            i = int((n - lower_bound) / bucket_size)
            if bucket_max[i] is None:
                bucket_max[i] = n
            else:
                bucket_max[i] = max(bucket_max[i], n)
            if bucket_min[i] is None:
                bucket_min[i] = n
            else:
                bucket_min[i] = min(bucket_min[i], n)
        
        max_gap = 0
        bucket_min = [m for m in bucket_min if m is not None]
        bucket_max = [m for m in bucket_max if m is not None]
        for i in range(len(bucket_min)-1):
            max_gap = max(max_gap, bucket_min[i+1] - bucket_max[i])

        return max_gap