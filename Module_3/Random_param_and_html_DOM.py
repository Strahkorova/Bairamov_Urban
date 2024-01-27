def test(*args):
    for i, arg in enumerate(args):
        if isinstance(arg, list):
            print('')
            if len(arg) != 0:
                print('Список ', arg, 'включает в себя ', len(arg), 'элементов.')
            else:
                print('Список пуст!')
        elif isinstance(arg, dict):
            print('')
            print('Вывод словаря ', arg, 'с индексом', i, 'по ключу')
            for key in arg:
                print('Ключу = ', key, 'соответствет значение = ', arg[key])
        else:
            print('')
            if isinstance(arg, int):
                print('Целочисленное число = ', arg)
            elif isinstance(arg, str):
                print('Текст = ', arg)
            elif isinstance(arg, float):
                print('Число с плавающей точкой = ', arg)
            else:
                print('Другой тип данных ', type(arg))


My_list = [1, 'Car', 'Cat', 1.2, [1, 2, 3]]
My_dict = {'a': 45, 'b': 95, 'c': 'work'}
My_dict_2 = {'A': 205, 'B': 905, 'C': 'play'}
My_dict_3 = {'green': [0, 128, 0], 'black': 0000, 'white': [55, 25, 255]}
My_dict_4 = {'run': 'бегать', 'jump': 'прыгать', 'fly': 'летать'}
My_dict_5 = {'read': 'читать', 'write': 'писать', 'listen': 'слушать', 'speak': 'говорить'}


def test_2(**kwargs):
    for key, value in kwargs.items():
        if isinstance(value, list):
            print('')
            if len(value) != 0:
                print('Список ', value, 'включает в себя ', len(value), 'элементов.')
            else:
                print('Список пуст!')
        elif isinstance(value, dict):
            print('')
            print('Вывод словаря из  ', value, 'с именованным параметром', key, 'по ключу')
            for key_1 in value:
                print('Ключу = ', key_1, 'соответствет значение = ', value[key_1])
        else:
            print('')
            if isinstance(value, int):
                print('Целочисленное число = ', value, 'соответсвует параметру - ', key)
            elif isinstance(value, str):
                print('Текст = ', value, 'соответсвует параметру - ', key)
            elif isinstance(value, float):
                print('Число с плавающей точкой = ', value, 'соответсвует параметру - ', key)
            else:
                print('Другой тип данных ', type(value))


test_2(elem_1 = My_dict, elem_2 = 45, elem_3 = 'яблоко', elem_4 = My_list)


test(My_dict, My_list, My_dict_3, 45, 'writer', My_dict_5)


def fac(n):
    if n == 1:
        print('Факториал n=1 всегда равен ')
        return 1
    my_factorial = fac(n=n-1)
    return n * my_factorial


#print(fac(9))
