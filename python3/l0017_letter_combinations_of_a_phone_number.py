from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_letter_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        def generateCombination(digits: str) -> List[str]:
            if len(digits) == 0:
                return []
            elif len(digits) == 1:
                return digit_to_letter_map[digits]
            result = []
            for r in generateCombination(digits[1:]):
                for c in digit_to_letter_map[digits[0]]:
                    result.append(c + r)
            return result
        
        return generateCombination(digits)