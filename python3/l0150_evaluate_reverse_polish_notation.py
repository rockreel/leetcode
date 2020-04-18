from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if t == '+':
                    r = op2 + op1
                elif t == '-':
                    r = op2 - op1
                elif t == '*':
                    r = op2 * op1
                else:
                    r = int(float(op2) / op1)
                stack.append(r)
        return stack.pop()