# percentage: 76.29%
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
            }
        if not digits:
            return []
        if len(digits) == 1:
            return digit_to_letters.get(digits, [])
        else:
            result = []
            for r in self.letterCombinations(digits[1:]):
                for l in digit_to_letters.get(digits[0]):
                    result.append(l+r)
        return result
