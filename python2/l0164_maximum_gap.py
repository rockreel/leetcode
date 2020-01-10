class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        if len(nums) == 2:
            return max(nums) - min(nums)
        
        # Setting up the buckets so that the max gap should not be less than
        # the bucket_length, so don't need to calulate gap within each bucket.
        import math  
        num_buckets = len(nums) - 1
        lower_bound = min(nums)
        upper_bound = max(nums) + 1
        bucket_length = int(math.ceil(float(upper_bound-lower_bound)/float(num_buckets)))
        if bucket_length == 0:
            return 0
        
        # Find min and max numbers in each bucket.
        bucket_min = [None for _ in range(num_buckets)]
        bucket_max = [None for _ in range(num_buckets)]
        for n in nums:
            if bucket_min[(n-lower_bound)/bucket_length] is None:
                bucket_min[(n-lower_bound)/bucket_length] = n
            else:
                bucket_min[(n-lower_bound)/bucket_length] = min(n, bucket_min[(n-lower_bound)/bucket_length])
            if bucket_max[(n-lower_bound)/bucket_length] is None:
                bucket_max[(n-lower_bound)/bucket_length] = n
            else:
                bucket_max[(n-lower_bound)/bucket_length] = max(n, bucket_max[(n-lower_bound)/bucket_length])

        # Filter buckets without numbers and find the max gap.
        bucket_min = [x for x in bucket_min if x is not None]
        bucket_max = [x for x in bucket_max if x is not None]
        max_gap = 0
        for i in range(len(bucket_min)-1):
            max_gap = max(max_gap, bucket_min[i+1] - bucket_max[i])
            
        return max_gap

