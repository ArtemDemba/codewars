def unique_in_order(sequence):
    if not sequence:
        return []
    result = [sequence[0], ]
    for index in range(1, len(sequence)):
        if sequence[index - 1] != sequence[index]:
            result.append(sequence[index])
    return result


print(unique_in_order([]))
