class Solution:
    """
    @param n: the length of strobogrammatic number
    @return: All strobogrammatic numbers
    """
    def findStrobogrammatic(self, n):
        # write your code here
        def generate_strobogrammatic(n):
            num_map = {
                '1': '1', '6': '9', '8': '8',
                '9': '6', '0': '0'
            }
            if n == 0:
                return ['']
            if n == 1:
                return [k for k in num_map.keys() if k not in ['6', '9']]
            nums = []
            for num in generate_strobogrammatic(n-2):
                for k, v in num_map.items():
                    nums.append(k + num + v)
            return nums
                    
        return [n for n in generate_strobogrammatic(n)
                if not n or len(n) == 1 or n[0] != '0']

