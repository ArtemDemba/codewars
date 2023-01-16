def is_valid_walk(walk: list):
    return len(walk) == 10 and walk.count('e') == walk.count('w') and walk.count('n') == walk.count('s')


print(is_valid_walk(['n', 'n', 's', 's', 'e', 'e', 'w', 'w', 'w', 'e']))
