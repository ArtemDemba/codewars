def find_outlier(integers: list):
    if integers[0] % 2 + integers[1] % 2 + integers[2] % 2 in (2, 3):
        return list(filter(lambda item: item % 2 == 0, integers))[0]
    else:
        return list(filter(lambda item: item % 2 == 1, integers))[0]


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))