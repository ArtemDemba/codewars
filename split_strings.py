def solution(s: str) -> list:
    if not s:
        return []
    result = [s[i: i + 2] for i in range(0, len(s), 2)]
    if len(result[-1]) == 1:
        result[-1] += '_'
    return result


print(solution(''))
