from string import whitespace


def strip_comments(string: str, markers: list[str]) -> str:
    lines = string.split('\n')
    result = []
    for line in lines:
        is_marker = False
        for indx, char in enumerate(line):
            if char in markers:
                q = line[:indx]
                result.append(q)
                is_marker = True
                break
        if not is_marker:
            result.append(line)
    for indx, line in enumerate(result):
        if line == '':
            result[indx] = '\n'
    return '\n'.join([i.rstrip(whitespace) for i in result])


print(strip_comments(", '\navocados strawberries avocados ?\nwatermelons avocados oranges bananas\n@ pears",
                     ['!', ',', '-', '=', '^', "'", '@', '?', '#']))
