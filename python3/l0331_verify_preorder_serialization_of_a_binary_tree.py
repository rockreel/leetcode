class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        count = 1
        nodes = preorder.split(',')
        for n in nodes:
            if count == 0:
                return False
            if n == '#':
                count -= 1
            else:
                count += 1
           
                
        return count == 0
