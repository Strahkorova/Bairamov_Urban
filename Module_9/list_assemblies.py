
def square(x):
    return x**2

def filter_item(x):
    return x % 2

my_list = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

out_filter = filter(filter_item, map(square, my_list))
print("Отфильтрованный список: ", list(out_filter))
