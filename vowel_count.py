def get_count(sentence: str) -> int:
    return sum(1 for i in sentence if i in 'aioue')


print(get_count('qwertyuioplkanjnvh'))
