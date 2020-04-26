class Solution:
    """
    @param num: a string
    @return: true if a number is strobogrammatic or false
    """
    def isStrobogrammatic(self, num):
        # write your code here
        num_map = {
            '1': '1', '6': '9', '8': '8',
            '9': '6', '0': '0'
        }
        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i] not in num_map or
                num[j] not in num_map or
                num_map[num[i]] != num[j] or
                num_map[num[j]] != num[i]):
                return False
            i += 1
            j -= 1
        return True
