n = abs(numerator)
        d = abs(denominator)
        r = n % d
        r_map = { r: 3 }
        digits = [
            '-' if numerator * denominator < 0 else '',
            str(n // d),
            '.'
        ]
        repeat = -1
        while r != 0:
            n = r * 10
            digits.append(str(n // d))
            r = n % d
            if r not in r_map:
                r_map[r] = len(digits)
            else:
                repeat = r_map[r]
                break
        
        if repeat != -1:
            digits.insert(repeat, '(')
            digits.append(')')
        if digits[-1] == '.':
            digits.pop()
        return ''.join(digits)
