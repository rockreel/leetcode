class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def operate(operand1, operand2, operator):
            if operator == '+':
                return int(operand1) + int(operand2)
            elif operator == '-':
                return int(operand1) - int(operand2)
            
        result, operator, curr_num = 0, '+', '0'
        stack = []
        for c in s:
            if c == '(':
                stack.append((result, operator))
                result, operator, curr_num = 0, '+', '0'
            elif c == ')':
                curr_num = operate(result, curr_num, operator)
                result, operator = stack.pop()
            elif c in ('+', '-'):
                result = operate(result, curr_num, operator)
                curr_num = '0'
                operator = c
            elif c != ' ':
                curr_num += c
        result = operate(result, curr_num, operator)
        
        return result

