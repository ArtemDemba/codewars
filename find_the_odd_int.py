from collections import Counter


def find_it(seq):
    c = Counter(seq)
    return [key for key in c.keys() if c[key] % 2 == 1][0]


print(find_it([1,1,2]))
