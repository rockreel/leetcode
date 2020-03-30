class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        pre_result = self.countAndSay(n-1)
        pre_n = ''
        count = 0
        result = ''
        for n in pre_result:
            if n != pre_n:
                if count != 0:
                    result += str(count) + pre_n
                pre_n = n
                count = 0
            count += 1
        result += str(count) + pre_n
        return result