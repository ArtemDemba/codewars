def is_pangram(s: str) -> bool:
    char_dict = {}
    for item in s.lower():
        if item.isalpha():
            char_dict[item] = True

    return len(char_dict) == 26


print(is_pangram('The quick, brown fox jumps over the lazy dog!'))
