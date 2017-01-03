class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
            
        last_number = None
        count = 0
        result = ''
        for c in self.countAndSay(n-1):
            if c != last_number:
                if last_number:
                    result += str(count) + last_number
                last_number = c
                count = 1
            else:
                count += 1
        result += str(count) + last_number
        return result

