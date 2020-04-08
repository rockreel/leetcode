class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num_result = 0
        base1 = 1
        for n1 in num1[::-1]:
            base2 = 1
            for n2 in num2[::-1]:
                num_result += (ord(n1) - 48) * base1 * (ord(n2) - 48) * base2
                base2 *= 10
            base1 *= 10
        result = ''
        while num_result > 0:
            result =  chr(num_result % 10 + 48) + result
            num_result //= 10
        return result if result else '0'