from functools import reduce


def persistence(n: int):
    stage = 0
    while n >= 10:
        n = reduce(lambda a, b: a * b, list(map(int, list(str(n)))))
        stage += 1
    return stage


print(persistence(25))
