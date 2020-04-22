class TwoSum:
    
    def __init__(self):
        self._nums = []
        
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        import bisect
        insert_pos = bisect.bisect_left(self._nums, number)
        self._nums.insert(insert_pos, number)

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        start, end = 0, len(self._nums) - 1
        while start < end:
            if self._nums[start] + self._nums[end] == value:
                return True
            elif self._nums[start] + self._nums[end] > value:
                end -= 1
            else:
                start += 1
        return False