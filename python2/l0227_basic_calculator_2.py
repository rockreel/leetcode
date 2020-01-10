class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import math
        curr_num = '0'
        operator = '+'
        stack = []
        for c in s+'+':
            if c == ' ':
                continue
            elif c in ('+', '-', '*', '/'):
                if operator == '+':
                    stack.append(int(curr_num))
                elif operator == '-':
                    stack.append(-int(curr_num))
                elif operator == '*':
                    stack[-1] *= int(curr_num)
                else:
                    if stack[-1] > 0:
                        stack[-1] = stack[-1] / int(curr_num)
                    else:  # Python negative division round towards minus infinity.
                        stack[-1] = -((-stack[-1]) / int(curr_num))
                curr_num = ''
                operator = c
            else:
                curr_num += c
        
        return sum(stack)

