def read_file(name):
    with open(name, 'r', encoding='utf-8') as f:
        text = f.read()
        text_2 = ''
        for el in text:
            if el.isalpha() or el == ' ':
                text_2 += el.lower()
    return [el for el in list(set(text_2.split())) if len(el) >= 2]


def save_file(name, list_words):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(f'Количество уникальных слов: {len(list_words)}\n')
        list_words.sort()
        for el in list_words:
            f.write(f'{el}\n')
