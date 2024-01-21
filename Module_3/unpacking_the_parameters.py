# Функция с параметрами по умолчанию
def print_param(a=1, b='word', c=True):
    print('Вывожу = ', a, b, c)


# print_param()
# print_param(a=1, b='word', c=True)
# print_param(a=1)
# print_param(a=1, c=True)

# print_param(b=25)
# print_param(c=[1, 2, 3])


# Распаковка параметров

values_list = [1, 'work', 1.2]

values_dict = {'a': 1, 'b': 'write', 'c': 10.2}

# print_param(*values_list)
# print_param(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = ['Red', 85]

print_param(*values_list_2, 45)
