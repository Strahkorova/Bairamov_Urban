def test():
    a = 4
    b = 5
    print('Произведение a на b = ', a * b)


test()


def test_2(x, y, z):
    print('Длина прямоугольника = ', x, ' м.')
    print('Ширина прямоугольника = ', y, ' м.')
    print('Высота прямоугольника = ', z, ' м.')
    print('Объем прямоугольника = ', x * y * z, 'м3')


dlina = int(input('Ввдите длину прямоугольника = '))
shirina = int(input('Ввдите ширину прямоугольника = '))
visota = int(input('Ввдите высоту прямоугольника = '))


test_2(dlina, shirina, visota)
