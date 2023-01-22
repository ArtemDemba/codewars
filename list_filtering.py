def filter_list(l: list) -> list:
    return [i for i in l if type(i) == int]


print(filter_list([1, 2, 'a', 'b']))
