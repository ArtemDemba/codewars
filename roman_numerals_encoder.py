def solution(n: int):
    result = ''
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    key = 0
    while key != len(roman_numerals.keys()):
        current_number = list(roman_numerals.keys())[key]
        if n - current_number >= 0:
            result += roman_numerals[list(roman_numerals.keys())[key]]
            n -= current_number
            key -= 1
        key += 1

    return result


print(solution(1))
