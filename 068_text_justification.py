class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        remain_length = maxWidth
        row = []
        i = 0

        for w in words:
            if len(w) <= remain_length:
                row.append(w)
                remain_length -= len(w) + 1
            else:
                # A row has filled up, format the string and add to result.
                num_spaces = remain_length + len(row)
                if len(row) == 1:
                    row_str = row[0] + ' ' * num_spaces
                else:
                    num_spaces_per_gap = num_spaces / (len(row) - 1)
                    num_extra_spaces = num_spaces % (len(row) - 1)
                    spaces = []
                    for j in range(len(row)-1):
                        spaces.append(' ' * num_spaces_per_gap + (' ' if j < num_extra_spaces else ''))
                    spaces.append('')
                    row_str = ''.join([x+y for x, y in zip(row, spaces)])
                result.append(row_str)
                
                # Add word to row.
                remain_length = maxWidth - len(w) - 1
                row = [w]
                
        # Append the last words.
        s = ' '.join(row)
        result.append(s + ' ' * (maxWidth - len(s)))
        
        return result

