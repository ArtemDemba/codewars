def likes(names: list[str]):
    length = len(names)
    if length == 0:
        return 'no one likes this'
    elif length == 1:
        return f'{names[0]} likes this'
    elif length == 2:
        return f'{" and ".join(names)} like this'
    elif length == 3:
        return f'{", ".join(names[:2])} and {names[2]} like this'
    else:
        return f'{", ".join(names[:2])} and {length - 2} others like this'


print(likes([]))
