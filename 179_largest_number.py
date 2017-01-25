class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        def compare(num1, num2):
            if num1 + num2 == num2 + num1:
                return 0
            elif num1 + num2 < num2 + num1:
                return -1
            else:
                return 1

        nums = sorted([str(n) for n in nums], cmp=compare, reverse=True)
        result = ''.join(nums)
        
        if result[0] == '0':
            return '0'
        else:
            return result

