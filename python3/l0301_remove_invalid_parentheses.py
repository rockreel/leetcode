from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        count = 0
        rm_left = 0
        rm_right = 0
        for c in s:
            if c == '(':
                if count < 0:
                    count = 1
                else:
                    count += 1
            elif c == ')':
                count -= 1
            else:
                continue
            if count < 0:
                rm_right += 1     
        rm_left = max(count, 0)
        
        def remove_parentheses(s, curr, count, rm_left, rm_right, valids):
            if not s:
                if rm_left == rm_right == 0 and count == 0:
                    valids.add(curr)
                return
            if s[0] == '(':
                if rm_left > 0:
                    remove_parentheses(s[1:], curr, count, rm_left-1, rm_right, valids)
                remove_parentheses(s[1:], curr+s[0], count+1, rm_left, rm_right, valids)
            elif s[0] == ')':
                if rm_right > 0:
                    remove_parentheses(s[1:], curr, count, rm_left, rm_right-1, valids)
                if count > 0:
                    remove_parentheses(s[1:], curr+s[0], count-1, rm_left, rm_right, valids)
            else:
                remove_parentheses(s[1:], curr+s[0], count, rm_left, rm_right, valids)
                
        valids = set()
        remove_parentheses(s, '', 0, rm_left, rm_right, valids)
        return list(valids)