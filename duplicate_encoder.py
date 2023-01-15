import collections


def duplicate_encode(word: str):
    word = word.lower()
    d = collections.Counter(word)
    return ''.join(['(' if d[i] == 1 else ')' for i in word])


print(duplicate_encode('(( @'))

