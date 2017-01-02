class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Scan every valid paren and put in a stack.
        open_paren_stack = []
        valid_paren_stack = []
        for i, c in enumerate(s):
            if c == '(':
                open_paren_stack.append(i)
            elif open_paren_stack:
                current_start_idx = open_paren_stack.pop()
                # Pop all intermediate paren out and push a complete one in.
                while valid_paren_stack and valid_paren_stack[-1][0] > current_start_idx:
                    valid_paren_stack.pop()
                valid_paren_stack.append((current_start_idx, i))
        
        # Go through all valid paren to find max concantenated length.
        max_length = 0
        current_start_idx = 0
        current_length = 0
        while valid_paren_stack:
            start_idx, end_idx = valid_paren_stack.pop()
            if current_start_idx - 1 == end_idx:
                current_length += end_idx - start_idx + 1
            else:
                current_length = end_idx - start_idx + 1
            current_start_idx = start_idx
            max_length = max(max_length, current_length)
                
        return max_length

