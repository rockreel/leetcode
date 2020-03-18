class Solution:
    def myAtoi(self, str: str) -> int:
        r = 0
        sign = 1
        start_parse = False
        for c in str:
            if not start_parse:
                if c in ' ':
                    continue
                elif c == '-':
                    sign = -1
                    start_parse = True
                elif c == '+':
                    start_parse = True
                elif c in '0123456789':
                    r = ord(c) - 48
                    start_parse = True
                else:
                    return 0
            else:
                if c in '0123456789':
                    r = r * 10 + ord(c) - 48
                else:
                    break
        r = sign * r 
        if r > 2**31 - 1:
            return 2**31-1
        if r < -2**31:
            return -2**31
        return r