class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                str_tokens = []
                while stack[-1] != '[':
                    str_tokens.append(stack.pop())
                stack.pop()
                num_tokens = []
                while stack and stack[-1] in '0123456789':
                    num_tokens.append(stack.pop())
                num = int(''.join(num_tokens[::-1]))
                ss = ''.join(str_tokens[::-1])
                stack.append(ss*num)
            else:
                stack.append(c)
        return ''.join(stack)