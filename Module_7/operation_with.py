from pprint import pprint


# file = open(file_name, mode='r', encoding='utf8')
# line = True
# while line:
#     line = file.readline()
#     if 'melting' in line:
#         print("слово melting в троке № = ", line)
#         break
# else:
#     print("Такого слова нет")
#
# file.close()


file_name = 'poem.txt'
with open(file_name, mode='r', encoding='utf8') as file:
    for line in file:
        print(line)
print(file.closed)

#with позволяет автоматически закрывать файл после прочтения