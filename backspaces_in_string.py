def clean_string(s):
    result_list = []
    for char in s:
        if char == '#':
            if not result_list:
                pass
            else:
                del result_list[-1]
        else:
            result_list.append(char)
    return ''.join(result_list)


print(clean_string('abc####d##c#'))
