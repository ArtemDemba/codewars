def digital_root(n: int):
    s = str(n)
    while len(s) != 1:
        s = str(sum(map(int, s)))
    return int(s)


