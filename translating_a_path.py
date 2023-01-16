def walk(path: str):
    if not path:
        return 'Paused'

    path_dict = {'v': 'down', '^': 'up', '>': 'right', '<': 'left'}
    amount = 1
    result = []

    for action_index in range(1, len(path) + 1):
        try:
            if path[action_index] != path[action_index - 1]:
                result.append(f'Take {amount} {"step" if amount == 1 else "steps"} {path_dict[path[action_index - 1]]}')
                amount = 1
            else:
                amount += 1
        except IndexError:
            result.append(f'Take {amount} {"step" if amount == 1 else "steps"} {path_dict[path[-1]]}')
            return '\n'.join(result)


print(walk('^^vvvv>><<^v>'))
