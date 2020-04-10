class Solution:
    def addBinary(self, a: str, b: str) -> str:
        pa, pb = len(a) - 1, len(b) - 1
        result = []
        c = '0'
        while pa >= 0 or pb >= 0:
            na = a[pa] if pa >= 0 else '0'
            nb = b[pb] if pb >= 0 else '0'
            if na == nb:
                result.append(c)
                c = na
            else:
                if c == '0':
                    result.append('1')
                else:
                    result.append('0')
            pa -= 1
            pb -= 1
        if c == '1':
            result.append(c)
        return ''.join(result[::-1])