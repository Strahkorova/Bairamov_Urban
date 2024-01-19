# -*- coding: utf-8 -*-

# block code

x, y = 10, 29

if x < 0:
    print('Х меньше нуля')
    z = x**2 + y
else:
    print('Х больше нуля')
    z = x - y
print('Result', z)

# ср. с С++
# вложенные блоки кода

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

# оператор pass

if x < 0:
    if y > 0:
        z = -x + y
    else:
        z = -x - y
else:
    z = x + y

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в python
# https://www.python.org/dev/peps/pep-0008/

# 4 spaces на каждый уровень отступа

if x < 0:
    if y > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

x = 2
y = x * x + 1
is_big = x >= 3000

x = my_poem[-1]
print(x)
my_list = [2, 3, 4, 5, 6,]

# reformat кода

number_1, number_2 = 3, 8

if number_1 == 3:
    print(42)

if number_1 < 0:
    if number_2 > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print('стой!')


# названия переменных

count_of_my_pets = 34
if count_of_my_pets > 10:
    print('I need more space for my pets!')

my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets_and_bird:
    print('Wow!')

MyFavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
var_1 = 34
var_2 = 43
if var_1 > var_2:
    print()
var_0 = 9
if var_0 > 0:
    print()


animals = ['cat', 'wolf', 'ostrich']
if 'lion' in animals:
    print('Wow!')
