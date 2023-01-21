def tribonacci(signature: list, n: int) -> list:
    result = []
    for i in range(n):
        if i < len(signature):
            result.append(signature[i])
        else:
            result.append(sum(result[-3:]))

    return result


print(tribonacci([0.5, 0.5, 0.5], 30))
