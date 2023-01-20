def pos_average(s: str) -> float:
    splitted_text = s.split(', ')
    all_letters_count, common_pos_count = 0, 0

    for index_1, first in enumerate(splitted_text):
        for index_2, second in enumerate(splitted_text):
            if index_1 >= index_2:
                continue
            for letter_first, letter_second in zip(first, second):
                if letter_first == letter_second:
                    common_pos_count += 1
                all_letters_count += 1
    return common_pos_count / all_letters_count * 100


print(pos_average('444996, 699990, 666690, 096904, 600644, 640646, 606469, 409694, 666094, 606490'))
