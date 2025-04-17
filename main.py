# Функция для подсчета количества гласных в строке
def count_vowels(s):
    vowels_list = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    count = 0
    for ch in s:
        if ch.lower() in vowels_list:
            count += 1
    return count