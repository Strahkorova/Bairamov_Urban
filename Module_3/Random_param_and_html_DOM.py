def test(args, kwargs):
    for key in kwargs:
        print('Ключу = ', key, 'соответствет значение = ', kwargs[key])
    if len(args) != 0:
        for i in args:
            if isinstance(i, int):
                print('Целочисленное число = ', i)
            elif isinstance(i, str):
                print('Текст = ', i)
            elif isinstance(i, list):
                print('Список включает = ', i)
            elif isinstance(i, float):
                print('Число с плавающей точкой = ', i)
            else:
                print('Другой тип данных ', type(i))
    else:
        print('Список пуст')


My_list = [1, 'Car', 'Cat', 1.2, [1, 2, 3]]
My_dict = {'a': 45, 'b': 95, 'c': 'work'}
#test(My_list, My_dict)



def fac(n):
    if n == 1:
        print('Факториал n=1 всегда равен ')
        return 1
    My_factorial = fac(n= n-1)
    return n * My_factorial


print(fac(9))