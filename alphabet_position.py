def alphabet_position(text: str):
    text = text.lower()
    return ' '.join([str(ord(x) - 96) for x in text if x.isalpha()])


print(alphabet_position('-39 -46 -42 -46 -47 -44 -42 -45 -44 -45'))
