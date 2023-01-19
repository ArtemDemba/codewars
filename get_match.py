import re


def find_matched_by_pattern(pattern: str):
    def wrap(string: str):
        pattern_match = ''
        for letter in pattern:
            pattern_match += '.*' + f'{letter}'
        pattern_match += '.*'
        print(pattern_match)
        return bool(re.match(rf'{pattern_match}', string))
    return wrap


a = find_matched_by_pattern('yjk')
b = a('skyjack')
print(b)
