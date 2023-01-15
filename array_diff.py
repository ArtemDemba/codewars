def array_diff(a: list, b: list):
    return [x for x in a if x not in b]


a = [1, 2, 1, 3, 1]
b = [1, 2]
a = array_diff(a, b)
print(a)