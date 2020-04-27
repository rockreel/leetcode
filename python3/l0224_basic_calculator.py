from typing import List

class Solution:

    def calculate(self, s: str) -> int:
        
        def calculate_stack(stack: List[int]) -> int:
            # Calculate result up to a ( or entire stack.
            r = 0
            while stack and stack[-1] != '(':
                num = stack.pop()
                op = stack.pop() if stack and stack[-1] != '(' else '+'
                if op == '+':
                    r += num
                else:
                    r -= num
            return r

        stack = []
        curr_num = ''
        for c in s:
            if c == ' ':
                continue
            if c == '(':
                stack.append(c)
            elif c == ')':
                stack.append(int(curr_num))
                # Calculate result back to last '('.
                r = calculate_stack(stack)
                # Pop out last '('.
                stack.pop()
                curr_num = str(r)
            elif c in '+-':
                stack.append(int(curr_num))
                stack.append(c)
                curr_num = ''
            else:
                curr_num = curr_num + c
        stack.append(int(curr_num))

        return calculate_stack(stack)