# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random


def generate_random_name():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        first_word = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        second_word = ''.join(random.choice(letters) for i in range(random.randint(1, 15)))
        yield f"{first_word} {second_word}"


gen = generate_random_name()
for i in range(5):
    print(next(gen))

# Здесь пишем код
