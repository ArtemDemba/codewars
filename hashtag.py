from string import capwords
from re import sub


def generate_hashtag(s: str):
    if len(s) > 140 or not s:
        print(len(s))
        return False
    result = '#' + sub(r' +', '', capwords(s))
    return result
