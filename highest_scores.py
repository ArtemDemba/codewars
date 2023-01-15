def high(x: str):
    words = x.split()
    d = dict()
    for word in words:
        scores = sum([ord(char) for char in word]) - len(word) * 96
        if scores not in d:
            d[scores] = word
    return d[max(d.keys())]


print(high('take me to semynak'))
