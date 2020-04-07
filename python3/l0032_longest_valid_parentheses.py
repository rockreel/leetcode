class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right = 0, 0
        max_length = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif right > left:
                left, right = 0, 0
        left, right = 0, 0
        for c in s[::-1]:
            if c == '(':
                left += 1
            else:
                right += 1
            if left == right:
                max_length = max(max_length, left + right)
            elif left > right:
                left, right = 0, 0
        return max_length
