x = 5

if x == 1:
    print('Hello')
    a = -5
    if a < 0:
        print('less than 0')
    print('Goodbye')

elif x == 2:
    a, b = 11, 6
    if a > b:
        print('a > b')
    if a > b and a > 0:
        print('success')
    if (a > b) and (a > 0 or b < 1000):
        print('success')
    if 5 < b < 10:
        print('success')

elif x == 3:
    if '45' > '145':
        print('success')
    if '145' > '15':
        print('success')
    if [1, 2] > [1, 1]:
        print('success')

elif x == 4:
    if '6' > 5:
        print('success')
    if [5, 6] > 5:
        print('success')
    if '6' != 5:
        print('success')

else:
    print('There is no correct vertification')
