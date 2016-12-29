# percentage 81.46%
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ''
        if numRows == 1:
            return s
        
        delta = 2*numRows - 2
        
        result = []
        
        for i in range(0, len(s), delta):
            result.append(s[i])
        
        for row in range(1, numRows-1):
            for i in range(row, len(s), delta):
                result.append(s[i])
                if i+delta-row*2 < len(s):
                    result.append(s[i+delta-row*2])
                
        for i in range(numRows-1, len(s), delta):
            result.append(s[i])
            
        return ''.join(result)
