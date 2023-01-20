def string_expansion(s: str) -> str:
    result = ''
    last_number = -1

    for index, char in enumerate(s):
        if char.isalpha():
            if index == 0:
                result += char
                continue
            if s[index - 1].isdigit():
                last_number = int(s[index - 1])
                result += char * last_number
            else:
                result += char if last_number == -1 else char * last_number
    return result


print(string_expansion('gb1Bd0f020ae40Db'))
