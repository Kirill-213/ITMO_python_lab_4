import random
import string

# функция генерации ключа
def key_generation():
    letters = string.ascii_uppercase   # получение всех буквенных символов
    numbers = [str(i) for i in range(10)]   # получение всех цифр

    value_interval = [12, 20]   # интервал суммы коэффициентов

    number_ratio = 1   # весовой коэф цифр
    letters_ratio = 2   # весовой коэф букв

    letters_amount = random.choice((range(2,12)))   # количество букв
    # цикл выбора подходящего кол-ва букв
    while (letters_ratio * letters_amount + (12- letters_amount) * number_ratio) not in range(value_interval[0], value_interval[1]):
        letters_amount = random.choice((range(3, 12)))  # количество букв

    # выбор кол-во букв в 1й части
    if letters_amount % 5 != 0:
        let_1 = random.choice(range(letters_amount % 5))
    else:
        let_1 = 4
    let_2 = random.choice(range(letters_amount - let_1))   # кол-во букв во 2й части
    let_3 = letters_amount - let_1 - let_2   # кол-во букв в 3ей части
    mass_1 = [let_1, let_2, let_3]   # список кол-во букв в каждой части
    mass = []   # итоговый ключ

    # цикл добавления элементов в каждую часть ключа
    for j in range(len(mass_1)):
        for i in range(mass_1[j]):
            mass.append(random.choice(letters))
        for i in range(4 - mass_1[j]):
            mass.append(random.choice(numbers))

    # итоговая версия ключа с разделением
    line = ''
    for i in range(1,13):
        line += mass[i - 1]
        if i == 4 or i == 8:
            line += '-'
    return line   # возвращение ключа из функции
