class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
            
        add_zero_first = True
        gray_codes = []
        for c in self.grayCode(n-1):
            if add_zero_first:
                gray_codes.append((c<<1) + 0)
                gray_codes.append((c<<1) + 1)
                add_zero_first = False
            else:
                gray_codes.append((c<<1) + 1)
                gray_codes.append((c<<1) + 0)
                add_zero_first = True
        return gray_codes

