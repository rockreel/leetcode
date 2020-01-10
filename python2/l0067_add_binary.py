class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import itertools
        result  = []
        c = 0
        for m, n in itertools.izip_longest(reversed(a), reversed(b), fillvalue='0'):
            r = int(m) + int(n) + c
            if r > 1:
                result.append(str(r-2))
                c = 1
            else:
                result.append(str(r))
                c = 0
        if c == 1:
            result.append('1')
        return ''.join(reversed(result))

