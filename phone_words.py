def phone_words(string_of_nums: str):
    string_of_nums += '1'
    convert_digit_to_letter = {
        '0': ' ',
        '1': 'dkvjpmsdio',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    amount = 0
    result = ''
    for digit in range(1, len(string_of_nums)):
        l = len(convert_digit_to_letter[string_of_nums[digit - 1]])
        if string_of_nums[digit] == string_of_nums[digit - 1]:
            amount += 1
            if amount > l - 1:
                result += convert_digit_to_letter[string_of_nums[digit - 1]][l - 1]
                amount = 0
            continue
        if string_of_nums[digit] == '1':
            result += convert_digit_to_letter[string_of_nums[digit - 1]][amount % l]
        else:
            if string_of_nums[digit - 1] != '1':
                result += convert_digit_to_letter[string_of_nums[digit - 1]][amount % l]
        amount = 0
    return result


test = '111'
print(phone_words(test))
print(test)
