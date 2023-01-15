def order(sentence: str):
    return ' '.join(sorted(sentence.split(), key=lambda digit: sorted(digit)[0]))
