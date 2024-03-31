

def string_to_int(s):
    try:
        return int(s)
    except ValueError:
        return f"Ошибка: невозможно преобразовать '{s}' в целое цисло."


def read_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл '{filename}' не найден."
    except IOError:
        return f"Ошибка ввода/вывода при работе с файлом '{filename}'."


def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль."
    except TypeError:
        return "Ошибка: аргументы должны быть числами."

def access_list_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return f"Ошибка: индекс {index} вне диапазона списка."
    except TypeError:
        return "Ошибка: индекс должен быть целым числом."


print(divide_numbers(5,0))
