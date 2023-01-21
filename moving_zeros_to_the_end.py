def move_zeros(lst: list) -> list:
    for item in lst:
        if item == 0:
            lst.remove(0)
            lst.append(0)
    return lst


test = []
result = move_zeros(test)
print(result)
