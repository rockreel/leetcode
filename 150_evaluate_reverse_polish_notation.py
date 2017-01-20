class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in '+-*/':
                op2 = stack.pop()
                op1 = stack.pop()
                if t == '+':
                    stack.append(op1+op2)
                elif t == '-':
                    stack.append(op1-op2)
                elif t == '*':
                    stack.append(op1*op2)
                else:
                    stack.append(abs(op1)/abs(op2)
                                 if op1*op2 > 0 else -(abs(op1)/abs(op2)))
            else:
                stack.append(int(t))
        return stack[0]
