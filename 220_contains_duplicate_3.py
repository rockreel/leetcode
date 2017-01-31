class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        from collections import OrderedDict
        num_map = OrderedDict()
        for n in nums:
            key = n/t if t != 0 else n
            if key in num_map:
                if abs(num_map[key] - n) <= t:
                    return True
            if key+1 in num_map:
                if abs(num_map[key+1] - n) <= t:
                    return True
            if key-1 in num_map:
                if abs(num_map[key-1] - n) <= t:
                    return True
            
            if k > 0:        
                if len(num_map) == k:
                    num_map.pop(next(iter(num_map)))
                num_map[key] = n
            
        return False

