immutable_var = (1, 2, 'do', 3, 5,)
print(immutable_var)

# immutable_var[1] = 4
# Изменение данных в кортеже не возможно, так как это неизменяемый объект
var = immutable_var + (7, 8)
print(var)
list = [26, 35, 4]
mutable_list = [4, 15, 8, 64]
mutable_list.extend(list)
print(mutable_list)
mutable_list.sort()
print(mutable_list)
