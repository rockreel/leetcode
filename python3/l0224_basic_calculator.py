class Solution:
    def calculate(self, s: str) -> int:

        def calculate_no_paren(s: str) -> int:
            return 0

        stack = []
        for i, c in s:
            if c == '(':
                stack.append(i)
            else:
                j = stack.pop()
                calculate_no_paren(s[j+1:i])
        return 0
       