def create_phone_number(n: list):
    return f'({"".join(map(str, n[:3]))}) {"".join(map(str, n[3:6]))}-{"".join(map(str, n[6:]))}'


def create_phone_number_prettier(n: list):
    return '({}{}{}) {}{}{}-{}{}{}'.format(*n)


print(create_phone_number_prettier([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
