class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        single_to_word = {
            1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
            16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
        }
        tenth_to_word = {
            2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
            6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety',
        }
        
        def number_to_words_base(n):
            # Convert 0 - 999 to English words.
            result = []
            if n/100 > 0:  # Hundred bit.
                result.append(single_to_word[n/100])
                result.append('Hundred')

            if n%100 > 0:  # Tenth and single bit.
                if n%100 < 10:
                    result.append(single_to_word[n%100])
                elif n%100 < 20:
                    result.append(single_to_word[n%100])
                else:
                    result.append(tenth_to_word[(n%100)/10])
                    if (n%100)%10:
                        result.append(single_to_word[(n%100)%10])
                        
            return ' '.join(result)
        
        if num == 0:
            return 'Zero'
        
        base = ['', 'Thousand', 'Million', 'Billion']
        result = []
        while num > 0:
            result.append(number_to_words_base(num%1000))
            num /= 1000

        return ' '.join(
            '%s %s' % (r, b) if b else r
            for r, b in reversed(zip(result, base)) if r)

