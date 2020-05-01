from typing import List

class Solution:
    def verifyPreorderN2(self, preorder):
        if not preorder:
            return True
            
        root = preorder[0]
        i, j = 1, len(preorder) - 1
        while i < len(preorder) and preorder[i] < root:
            i += 1
        while j >= 0 and preorder[j] > root:
            j -= 1
        if i - j != 1:
            return False
        return (
            self.verifyPreorder(preorder[1:i]) and
            self.verifyPreorder(preorder[i:])
        )
        
    def verifyPreorder(self, preorder):
        if not preorder:
            return True
        
        stack = []
        root = float('-inf')
        for n in preorder:
            if n < root:
                return False
            
            while stack and n > stack[-1]:
                root = stack.pop()
            stack.append(n)
        
        return True
